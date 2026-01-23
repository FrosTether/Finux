// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title Frost Protocol (FSZT)
 * @dev "Zero-Kelvin" Gas Optimized Implementation
 * @author Jacob Frost (FrosTether)
 */
contract FrostEther {
    
    // --- 1. METADATA (Storage Constants) ---
    string public constant name = "Frost Sub-Zero Time";
    string public constant symbol = "FSZT";
    uint8 public constant decimals = 18;
    
    // --- 2. OPTIMIZED STORAGE (Variable Packing) ---
    // We pack supply and owner data to save storage slots.
    uint256 private _totalSupply;
    address private _owner;
    
    // --- 3. MAPPINGS ---
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // --- 4. CUSTOM ERRORS (Gas Saver: No long error strings) ---
    error InsufficientBalance(uint256 available, uint256 required);
    error InsufficientAllowance(uint256 current, uint256 required);
    error InvalidReceiver();
    error Unauthorized();

    // --- 5. EVENTS ---
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor() {
        // Initial Supply: 25,000,000.31337
        // (Calculated in Wei: 25000000313370000000000000)
        _mint(msg.sender, 25000000313370000000000000);
        _owner = msg.sender;
    }

    // --- VIEW FUNCTIONS (Free to query) ---
    
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }

    // --- TRANSACTION FUNCTIONS (Gas Optimized) ---

    function transfer(address to, uint256 amount) external returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        uint256 currentAllowance = _allowances[from][msg.sender];
        
        if (currentAllowance != type(uint256).max) {
            if (currentAllowance < amount) revert InsufficientAllowance(currentAllowance, amount);
            
            // Unchecked: We just checked that allowance >= amount
            unchecked {
                _approve(from, msg.sender, currentAllowance - amount);
            }
        }

        _transfer(from, to, amount);
        return true;
    }

    // --- INTERNAL LOGIC (The Mathematical Core) ---

    function _transfer(address from, address to, uint256 amount) internal {
        if (to == address(0)) revert InvalidReceiver();

        uint256 fromBalance = _balances[from];
        
        // Gas Optimization: Custom Error instead of require string
        if (fromBalance < amount) revert InsufficientBalance(fromBalance, amount);

        // Gas Optimization: "Unchecked" Block
        // Since we already checked (fromBalance < amount), mathematical underflow is impossible.
        // Skipping the safety check here saves significant gas.
        unchecked {
            _balances[from] = fromBalance - amount;
            _balances[to] += amount;
        }

        emit Transfer(from, to, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        if (owner == address(0) || spender == address(0)) revert InvalidReceiver();
        
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    function _mint(address account, uint256 amount) internal {
        if (account == address(0)) revert InvalidReceiver();

        _totalSupply += amount;
        
        unchecked {
            _balances[account] += amount;
        }
        emit Transfer(address(0), account, amount);
    }
}
// Security Gating for Grayson's Wallet
function authorizeGPay(uint256 amount, bytes32 terminalID) external onlyKernel {
    require(msg.sender == FINUX_KERNEL_ADDRESS, "Unauthorized: Physical Kernel Sign-off Required");
    
    // Only allow spending from the "Spending" sub-vault
    require(amount <= spendingLimit, "Exceeds 3-second safety limit");
    
    // Update Cold Storage State
    vaultBalance -= amount;
    emit ColdStoragePurchase(terminalID, amount);
}
