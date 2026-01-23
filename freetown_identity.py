// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/721/extensions/ERC721Enumerable.sol";

contract FreetownIdentity is ERC721Enumerable {
    uint256 public nextTokenId;
    address public architect = 0xJACOB_FROST_ROOT;

    constructor() ERC721("Freetown Citizen", "FTZN") {}

    // Only the Architect or a designated Official can mint passports
    function issuePassport(address resident) public {
        require(msg.sender == architect, "Sovereignty: Unauthorized");
        _safeMint(resident, nextTokenId);
        nextTokenId++;
    }

    // Passports are Soulbound (Non-Transferable)
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal virtual {
        require(from == address(0) || to == address(0), "Identity: Passports are non-transferable.");
    }
}
