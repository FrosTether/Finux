// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract FrostPlat is ERC20, ERC20Burnable, AccessControl {
    bytes32 public constant BANK_HUB_ROLE = keccak256("BANK_HUB_ROLE");
    
    // Mapping of Physical Bar IDs to Token Batches
    mapping(bytes32 => bool) public vaultedBars;

    constructor() ERC20("Frost Platinum Dollar", "FRP") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Redeems digital tokens for physical platinum.
     * Can only be triggered by an authorized Bank Hub after scanning 
     * a valid Paperogram private key.
     */
    function redeemForPhysical(address citizen, uint256 amount, bytes32 paperogramHash) 
        external 
        onlyRole(BANK_HUB_ROLE) 
    {
        // 1. Checks: Ensure the paperogram hasn't been redeemed already
        require(!vaultedBars[paperogramHash], "Error: Physical asset already redeemed.");

        // 2. Effects: Burn the tokens from the citizen's balance
        _burn(citizen, amount);
        vaultedBars[paperogramHash] = true;

        // 3. Interactions: Emit event for the physical vault release
        emit PhysicalRedemption(citizen, amount, paperogramHash);
    }

    event PhysicalRedemption(address indexed citizen, uint256 amount, bytes32 paperogram);
}
