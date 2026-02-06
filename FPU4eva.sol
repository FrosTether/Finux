// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Fpu4eva is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 400_000_000 * 10**18; // 400 Million FPU
    uint256 public constant MINT_LIMIT = 100_000 * 10**18;    // 100k per transaction
    bool public mintActive = true;

    constructor() ERC20("Frost Processing Unit", "FPU4EVA") Ownable(msg.sender) {
        // Reserve 20% for Dev/Frost Protocol
        _mint(msg.sender, 80_000_000 * 10**18);
    }

    function surgeMint() external {
        require(mintActive, "Mint is paused");
        require(totalSupply() + MINT_LIMIT <= MAX_SUPPLY, "Max supply reached");
        
        _mint(msg.sender, MINT_LIMIT);
    }

    function toggleMint() external onlyOwner {
        mintActive = !mintActive;
    }
}
