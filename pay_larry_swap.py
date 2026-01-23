import time
import json
import requests
import sys
from web3 import Web3

# --- CONFIGURATION ---
RPC_URL = "https://mainnet.base.org"
MY_ADDRESS = "YOUR_WALLET_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY" # ⚠️ KEEP SAFE

# Target Amount to Pay Larry (in USD)
TARGET_USD = 900.0

# Base Network Addresses
WETH_ADDRESS = "0x4200000000000000000000000000000000000006"
USDC_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
ROUTER_ADDRESS = "0x2626664c2603336E57B271c5C0b26F421741e481" # Uniswap V3 Router

# --- SETUP ---
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("❌ Failed to connect to Base Network.")
    sys.exit()

def get_eth_price():
    """Fetches live ETH price from CoinGecko API."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url).json()
        price = response['ethereum']['usd']
        print(f"📉 Current ETH Price: ${price}")
        return price
    except Exception as e:
        print(f"❌ Error fetching price: {e}")
        sys.exit()

def get_eth_amount_for_usd(usd_amount, current_price):
    """Calculates how much ETH is needed for $900."""
    eth_needed = usd_amount / current_price
    # Add 1% buffer for gas/slippage
    eth_needed_safe = eth_needed * 1.01 
    print(f"🧮 Calculation: ${usd_amount} = {eth_needed:.4f} ETH")
    return w3.to_wei(eth_needed_safe, 'ether')

def swap_eth_for_usdc(amount_in_wei):
    """Executes the swap on Uniswap."""
    
    # Router ABI (Minimal)
    router_abi = json.loads('[{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"}]')
    
    router = w3.eth.contract(address=ROUTER_ADDRESS, abi=router_abi)
    
    print("🔄 Initiating Swap on Blockchain...")
    
    # Swap Parameters
    params = (
        WETH_ADDRESS,
        USDC_ADDRESS,
        3000,           # 0.3% Fee Tier
        MY_ADDRESS,     # Recipient (Send USDC back to you)
        int(time.time()) + 600, # 10 min deadline
        amount_in_wei,  # Amount of ETH to sell
        0,              # Min Out (Set to 0 for demo)
        0               # SqrtPriceLimit
    )
    
    # Build Transaction
    tx = router.functions.exactInputSingle(params).build_transaction({
        'from': MY_ADDRESS,
        'value': amount_in_wei, # Sending ETH value
        'nonce': w3.eth.get_transaction_count(MY_ADDRESS),
        'gas': 250000,
        'gasPrice': w3.eth.gas_price
    })
    
    # Sign & Send
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"✅ SWAP COMPLETE! TX Hash: {w3.to_hex(tx_hash)}")
    print(f"💰 You now have $900 USDC in your wallet.")

if __name__ ==
