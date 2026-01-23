import sys
import json
import time
from web3 import Web3

# --- CONFIGURATION (YOU MUST EDIT THIS) ---
# 1. RPC URL (Base Mainnet)
RPC_URL = "https://mainnet.base.org" 
# 2. Your Wallet Details
MY_ADDRESS = "YOUR_WALLET_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"  # ⚠️ KEEP SAFE

# 3. Token Addresses (Base Network Examples)
# WETH (Wrapped Ether) - The "From" Token
TOKEN_IN = "0x4200000000000000000000000000000000000006"
# USDC (USD Coin) - The "To" Token (Equivalent to Dollars)
TOKEN_OUT = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"

# 4. Router Address (Uniswap V3 Router on Base)
ROUTER_ADDRESS = "0x2626664c2603336E57B271c5C0b26F421741e481"

# --- SETUP ---
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("❌ Failed to connect to Blockchain.")
    sys.exit()

print(f"✅ Connected to Base. Active Address: {MY_ADDRESS}")

# Minimal ERC20 ABI (Approve & Transfer)
erc20_abi = json.loads('[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

# Minimal Router ABI (ExactInputSingle)
router_abi = json.loads('[{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"}]')

def approve_token(amount):
    """Authorize the Router to spend your Token"""
    print("1. Approving Token Spend...")
    token_contract = w3.eth.contract(address=TOKEN_IN, abi=erc20_abi)
    
    tx = token_contract.functions.approve(ROUTER_ADDRESS, amount).build_transaction({
        'from': MY_ADDRESS,
        'nonce': w3.eth.get_transaction_count(MY_ADDRESS),
        'gasPrice': w3.eth.gas_price
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"   Authorized! TX: {w3.to_hex(tx_hash)}")
    time.sleep(5) # Wait for confirmation

def execute_swap(amount_in_wei):
    """Executes the swap via Smart Contract"""
    print("2. Executing Swap...")
    router_contract = w3.eth.contract(address=ROUTER_ADDRESS, abi=router_abi)
    
    # Swap Parameters
    params = (
        TOKEN_IN,
        TOKEN_OUT,
        3000,           # Fee (0.3%)
        MY_ADDRESS,     # Recipient
        int(time.time()) + 600, # Deadline (10 mins)
        amount_in_wei,  # Amount to Swap
        0,              # Min Amount Out (Set to 0 for demo, use slippage in prod)
        0               # SqrtPriceLimit
    )
    
    tx = router_contract.functions.exactInputSingle(params).build_transaction({
        'from': MY_ADDRESS,
        'value': amount_in_wei if TOKEN_IN == "0x..." else 0, # Send ETH value if swapping native ETH
        'nonce': w3.eth.get_transaction_count(MY_ADDRESS),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"✅ Swap Sent! TX: {w3.to_hex(tx_hash)}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Amount to swap (e.g., 0.1 Tokens)
    # You must adjust decimals! USDC is 6 decimals, ETH is 18.
    amount_to_swap = w3.to_wei(0.1, 'ether') 
    
    try:
        approve_token(amount_to_swap)
        execute_swap(amount_to_swap)
    except Exception as e:
        print(f"❌ Error: {e}")
