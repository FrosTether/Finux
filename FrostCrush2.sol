// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IERC20Mintable {
    function mint(address to, uint256 amount) external;
}

contract FrostCrush2 {
    /*//////////////////////////////////////////////////////////////
                                CONSTANTS
    //////////////////////////////////////////////////////////////*/

    uint256 public constant EPOCH_TIME = 150; // seconds
    uint256 public constant HALVING_INTERVAL = 178_848_000; // 5y 8m
    uint256 public constant BASE_REWARD = 6685e15; // 6.685 * 1e18

    uint256 public constant MIN_TARGET = 2**224; // easiest
    uint256 public constant MAX_TARGET = 2**16;  // hardest

    /*//////////////////////////////////////////////////////////////
                                STORAGE
    //////////////////////////////////////////////////////////////*/

    IERC20Mintable public immutable FTC;

    uint256 public genesisTimestamp;
    uint256 public difficultyTarget;
    uint256 public lastEpochTimestamp;

    struct Epoch {
        uint256 participants;
        bool finalized;
    }

    mapping(uint256 => Epoch) public epochs;
    mapping(uint256 => mapping(address => bool)) public submitted;
    mapping(uint256 => mapping(address => bool)) public claimed;
    mapping(bytes32 => bool) public usedHashes;

    /*//////////////////////////////////////////////////////////////
                                EVENTS
    //////////////////////////////////////////////////////////////*/

    event WorkSubmitted(uint256 indexed epoch, address indexed miner);
    event RewardClaimed(uint256 indexed epoch, address indexed miner, uint256 amount);
    event DifficultyAdjusted(uint256 newTarget);

    /*//////////////////////////////////////////////////////////////
                                CONSTRUCTOR
    //////////////////////////////////////////////////////////////*/

    constructor(address _ftc) {
        FTC = IERC20Mintable(_ftc);
        genesisTimestamp = block.timestamp;
        lastEpochTimestamp = block.timestamp;
        difficultyTarget = MIN_TARGET;
    }

    /*//////////////////////////////////////////////////////////////
                                VIEW LOGIC
    //////////////////////////////////////////////////////////////*/

    function currentEpoch() public view returns (uint256) {
        return (block.timestamp - genesisTimestamp) / EPOCH_TIME;
    }

    function epochEnded(uint256 epochId) public view returns (bool) {
        return currentEpoch() > epochId;
    }

    function epochReward(uint256 epochId) public view returns (uint256) {
        uint256 era =
            ((epochId * EPOCH_TIME) / HALVING_INTERVAL);
        return BASE_REWARD >> era;
    }

    /*//////////////////////////////////////////////////////////////
                                MINING
    //////////////////////////////////////////////////////////////*/

    function submitWork(bytes32 hash) external {
        uint256 epochId = currentEpoch();

        require(!submitted[epochId][msg.sender], "One submit per epoch");
        require(!usedHashes[hash], "Hash already used");
        require(uint256(hash) < difficultyTarget, "Invalid work");

        submitted[epochId][msg.sender] = true;
        usedHashes[hash] = true;
        epochs[epochId].participants += 1;

        emit WorkSubmitted(epochId, msg.sender);
    }

    /*//////////////////////////////////////////////////////////////
                                CLAIM
    //////////////////////////////////////////////////////////////*/

    function claim(uint256 epochId) external {
        require(epochEnded(epochId), "Epoch active");
        require(submitted[epochId][msg.sender], "No submission");
        require(!claimed[epochId][msg.sender], "Already claimed");

        Epoch storage e = epochs[epochId];
        require(e.participants > 0, "No participants");

        uint256 reward =
            epochReward(epochId) / e.participants;

        claimed[epochId][msg.sender] = true;
        FTC.mint(msg.sender, reward);

        emit RewardClaimed(epochId, msg.sender, reward);
    }

    /*//////////////////////////////////////////////////////////////
                        DIFFICULTY ADJUSTMENT
    //////////////////////////////////////////////////////////////*/

    function finalizeEpoch(uint256 epochId) external {
        require(epochEnded(epochId), "Epoch not finished");
        Epoch storage e = epochs[epochId];
        require(!e.finalized, "Already finalized");

        uint256 actualTime =
            block.timestamp - lastEpochTimestamp;

        // Adjust difficulty between epochs
        difficultyTarget =
            difficultyTarget * actualTime / EPOCH_TIME;

        // Clamp
        if (difficultyTarget > MIN_TARGET) {
            difficultyTarget = MIN_TARGET;
        }
        if (difficultyTarget < MAX_TARGET) {
            difficultyTarget = MAX_TARGET;
        }

        // Failsafe: no one solved
        if (e.participants == 0) {
            difficultyTarget = MIN_TARGET;
        }

        lastEpochTimestamp = block.timestamp;
        e.finalized = true;

        emit DifficultyAdjusted(difficultyTarget);
    }
}