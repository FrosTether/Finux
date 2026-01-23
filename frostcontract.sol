// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFrostCoin {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract FrostGovernance {
    IFrostCoin public frostToken;
    address public leadDeveloper;
    uint256 public constant LEAD_DEV_WEIGHT = 5; // 5% Governance Stake

    struct Proposal {
        uint id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    mapping(uint => Proposal) public proposals;
    uint public proposalCount;

    // Events
    event NewProposal(uint id, string description);
    event VoteCast(uint id, address voter, uint256 weight, bool support);

    constructor(address _tokenAddress, address _leadDeveloper) {
        frostToken = IFrostCoin(_tokenAddress);
        leadDeveloper = _leadDeveloper;
    }

    // Create a proposal for a Protocol Change
    function createProposal(string memory _description) external {
        proposalCount++;
        Proposal storage p = proposals[proposalCount];
        p.id = proposalCount;
        p.description = _description;
        p.executed = false;
        emit NewProposal(proposalCount, _description);
    }

    // Voting Function
    function vote(uint _proposalId, bool _support) external {
        Proposal storage p = proposals[_proposalId];
        require(!p.hasVoted[msg.sender], "Already voted.");
        require(!p.executed, "Proposal already closed.");

        uint256 voterWeight = frostToken.balanceOf(msg.sender);

        // THE 5% RULE:
        // If the voter is the Lead Developer, add 5% of Total Supply to their weight
        if (msg.sender == leadDeveloper) {
            uint256 totalSupply = frostToken.totalSupply();
            uint256 governanceBonus = (totalSupply * LEAD_DEV_WEIGHT) / 100;
            voterWeight += governanceBonus;
        }

        require(voterWeight > 0, "No voting power.");

        if (_support) {
            p.votesFor += voterWeight;
        } else {
            p.votesAgainst += voterWeight;
        }

        p.hasVoted[msg.sender] = true;
        emit VoteCast(_proposalId, msg.sender, voterWeight, _support);
    }
}
