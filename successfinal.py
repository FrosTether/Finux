// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ImperialSuccessionV7 {
    struct CouncilMember {
        address wallet;
        uint256 weight; // Weights stored with 4 decimal precision (x10,000)
    }

    mapping(string => CouncilMember) public council;
    uint256 public constant QUORUM = 660000; // 66.0000% supermajority

    constructor() {
        council["Kyle_Gerdling"] = CouncilMember(0xKYLE_WALLET, 250000);
        council["Grayson_Gerdling"] = CouncilMember(0xGRAYSON_WALLET, 150000);
        council["Deacon_Frost"] = CouncilMember(0xDEACON_WALLET, 150000);
        council["Taylor_Andres_Gerdling"] = CouncilMember(0xTAYLOR_WALLET, 150000);
        council["Stephanie_Perry_Frost"] = CouncilMember(0xSTEPHANIE_WALLET, 100000);
        council["Kelsee_Missler"] = CouncilMember(0xKELSEE_WALLET, 80000);
        council["Kevin"] = CouncilMember(0xKEVIN_WALLET, 50000);
        council["Mitchell_Lee_Frost"] = CouncilMember(0xMITCHELL_WALLET, 31337);
        council["Chuck"] = CouncilMember(0xCHUCK_WALLET, 28663);
        council["Angel_Perez"] = CouncilMember(0xANGEL_WALLET, 10000);
    }

    function checkConsensus(string[] memory signers) public view returns (bool) {
        uint256 totalWeight = 0;
        for (uint256 i = 0; i < signers.length; i++) {
            totalWeight += council[signers[i]].weight;
        }
        return totalWeight >= QUORUM;
    }
}
