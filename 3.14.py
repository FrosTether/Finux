// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FrostCoin is ERC20, Ownable {
    // Precision: 10^10 → gives us about 10 decimal places of accuracy for 3π
    uint256 constant PI_APPROX = 94247779607;     // 3 * π * 10^10  ≈ 94247779607.6938 (truncated)
    uint256 constant PRECISION  = 10_000_000_000; // 10^10

    event TunnelCrossed(address indexed recipient, uint256 dogeAmount, uint256 frstAmount, string source);

    constructor() ERC20("FrostCoin", "FRST") Ownable(msg.sender) {}

    /**
     * @dev Mint FRST from DOGE deposit (called by trusted oracle/bridge)
     * @param recipient Who gets the FRST (linked or mirrored address)
     * @param dogeAmount Amount of DOGE in satoshis (8 decimals)
     */
    function mintFromDoge(address recipient, uint256 dogeAmount) external onlyOwner {  // or onlyOracle role
        // frstAmount = dogeAmount * 3π   (with dogeAmount in satoshis → FRST gets 18 decimals typically)
        // So: (dogeAmount * PI_APPROX) / PRECISION
        uint256 frstAmount = (dogeAmount * PI_APPROX) / PRECISION;

        _mint(recipient, frstAmount);

        emit TunnelCrossed(recipient, dogeAmount, frstAmount, "DogeVault → Pi Freeze");
    }

    // Optional: view function for current ratio (for frontend)
    function currentPiMultiplier() external pure returns (uint256 ratio, uint256 precision) {
        return (PI_APPROX, PRECISION);
    }
}