// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FrostCoin is ERC20, Ownable {
    // High-precision π approximation: π * 10^20 ≈ 314159265358979323846 (floor-truncated for integer math)
    // This gives ~20 decimal places of π accuracy
    uint256 constant PI_APPROX = 314159265358979323846;
    uint256 constant PRECISION = 100000000000000000000; // 10^20

    event TunnelCrossed(address indexed recipient, uint256 dogeAmount, uint256 frstAmount, string source);

    constructor() ERC20("FrostCoin", "FRST") Ownable(msg.sender) {
        // Optional: Pre-mint or set caps if desired
    }

    /**
     * @dev Mint FRST from DOGE deposit (called by trusted oracle/bridge)
     * @param recipient Who gets the FRST (linked or mirrored address)
     * @param dogeAmount Amount of DOGE in satoshis (8 decimals)
     */
    function mintFromDoge(address recipient, uint256 dogeAmount) external onlyOwner {
        // Formula: frstAmount = (dogeAmount * PI_APPROX) / PRECISION
        // Accounts for DOGE (8 decimals) → FRST (18 decimals): effective multiplier = π * 10^(18-8) internally
        // But since we input satoshis, this yields FRST wei = doge_sats * π (with precision adjustment)
        uint256 frstAmount = (dogeAmount * PI_APPROX) / PRECISION;

        require(frstAmount > 0, "Mint amount too small");

        _mint(recipient, frstAmount);

        emit TunnelCrossed(recipient, dogeAmount, frstAmount, "DogeVault -> Pi Perfection Freeze");
    }

    // View function for transparency (e.g., frontend display)
    function getPiMultiplier() external pure returns (uint256 approx, uint256 precision) {
        return (PI_APPROX, PRECISION);
    }

    // Optional: Add a claim function for mirrored addresses
    // Example: User signs a message with Doge key to prove ownership
    function claimMirrored(address mirrored, bytes calldata signature, uint256 nonce) external {
        // Implement ECDSA recovery or similar to verify Doge ownership
        // Then: transferFrom(mirrored, msg.sender, balanceOf(mirrored))
        revert("Claim logic to be implemented");
    }
}