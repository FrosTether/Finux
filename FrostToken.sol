// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract FrostToken is ERC20, ERC20Burnable, Pausable, AccessControl {
    // 1. ROLES
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant FREEZER_ROLE = keccak256("FREEZER_ROLE");

    constructor() ERC20("Frostcoin", "FTC") {
        // Grant the deployer (You) all permissions initially
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
        _grantRole(FREEZER_ROLE, msg.sender);
        
        // Initial Supply: 10 Million FTC to the Treasury
        _mint(msg.sender, 10000000 * 10 ** decimals());
    }

    // 2. THE GATEWAY FUNCTION
    // This is what your Python Bridge calls when Google Pay succeeds.
    // Only an address with 'MINTER_ROLE' can call this.
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }

    // 3. SECURITY & EMERGENCY
    function pause() public onlyRole(FREEZER_ROLE) {
        _pause();
    }

    function unpause() public onlyRole(FREEZER_ROLE) {
        _unpause();
    }

    // Required override for Solidity compiler
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        whenNotPaused
        override
    {
        super._beforeTokenTransfer(from, to, amount);
    }
}
