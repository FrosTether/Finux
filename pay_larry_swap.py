import time
import json
import requests
import sys
from web3 import Web3

# Import your Ledger Module
try:
    import ledger
except ImportError:
    print("⚠️  Warning: 'ledger.py' not found. Transaction won't be saved to CSV.")
    ledger = None

# --- CONFIGURATION ---
RPC_URL = "https://mainnet.base.org"
MY_ADDRESS = "YOUR_WALLET_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY" # ⚠️ KEEP SAFE

# Payment Details
TARGET_USD = 900.0
RECIPIENT_NAME = "Uncle Larry"
NOTE = "Atomic Swap (ETH -> USDC) for Cash Out"

# Base Network Addresses
WETH_ADDRESS = "0x4200000000000000000000000000000000000006"
USDC_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
ROUTER_ADDRESS = "0x2626664c2603336E57B271c5C0b26F421741e481" 

# --- SETUP ---
w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("❌ Failed to connect to Base Network.")
    sys.exit()

def get_eth_price():
    """Fetches live ETH price."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        response = requests.get(url).json()
        return response['ethereum']['usd']
    except:
        print("⚠️  API Error. Using fallback price $3000 (Adjust in code).")
        return 3000.0

def swap_and_log(amount_in_wei, usd_value):
    """Executes swap and logs to ledger on success."""
    
    # 1. Prepare Transaction
    router_abi = json.loads('[{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"}]')
    router = w3.eth.contract(address=ROUTER_ADDRESS, abi=router_abi)
    
    print("🔄 Sending Transaction to Blockchain...")
    
    params = (
        WETH_ADDRESS, USDC_ADDRESS, 3000, MY_ADDRESS, int(time.time()) + 600,
        amount_in_wei, 0, 0
    )
    
    tx = router.functions.exactInputSingle(params).build_transaction({
        'from': MY_ADDRESS,
        'value': amount_in_wei, 
        'nonce': w3.eth.get_transaction_count(MY_ADDRESS),
        'gas': 300000,
        'gasPrice': w3.eth.gas_price
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"⏳ Transaction Sent: {w3.to_hex(tx_hash)}")
    print("   Waiting for confirmation (approx 15s)...")
    
    # 2. Wait for Receipt (To confirm success)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    if receipt.status == 1:
        print("✅ SWAP CONFIRMED!")
        print(f"💰 Balance Updated: +${usd_value} USDC")
        
        # 3. Auto-Log to Ledger
        if ledger:
            print("\n📝 writing to ledger...")
            ledger.log_transaction(
                recipient=RECIPIENT_NAME,
                amount=usd_value,
                method="Crypto Swap (Base)",
                note=f"{NOTE} | TX: {w3.to_hex(tx_hash)[:10]}..."
            )
            print("✅ Saved to finux_ledger.csv")
    else:
        print("❌ Transaction Failed on-chain.")

if __name__ == "__main__":
    print(f"--- 💸 PAY {RECIPIENT_NAME.upper()} PROCESSOR 💸 ---")
    
    price = get_eth_price()
    print(f"📉 ETH Price: ${price}")
    
    # Calculate ETH needed (with 1% buffer)
    eth_amount = (TARGET_USD / price) * 1.01
    wei_amount = w3.to_wei(eth_amount, 'ether')
    
    print(f"🎯 Target: ${TARGET_USD} USDC")
    print(f"💳 Cost:   {eth_amount:.5f} ETH")
    
    confirm = input("\nExecute Swap & Record to Ledger? (y/n): ")
    if confirm.lower() == 'y':
        swap_and_log(wei_amount, TARGET_USD)
    else:
        print("Cancelled.")
