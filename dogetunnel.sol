    function mintFromDoge(address recipient, uint256 dogeAmount) external onlyOracle {
        // CORRECTION: Direct Elite Multiplier
        // 1 DOGE = 3.1337 FRST
        // Calculation: (DOGE * 31337) / 10000
        
        // Example: 1,000,000 DOGE * 31337 = 31,337,000,000
        // Divide by 10,000 = 3,133,700 FRST
        
        uint256 numerator = dogeAmount * 31337;
        uint256 denominator = 10000;
        uint256 frstAmount = numerator / denominator;

        _mint(recipient, frstAmount);
        
        emit TunnelCrossed(recipient, dogeAmount, frstAmount, "DogeVault");
    }
