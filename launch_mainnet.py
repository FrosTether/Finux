import os
import sys
import json
import time
from web3 import Web3
from solcx import compile_standard, install_solc

# --- CONFIGURATION (EDIT THIS SECTION CAREFULLY) ---
# 1. The Chain you are launching on.
#    - Ethereum Mainnet: "https://mainnet.infura.io/v3/YOUR_INFURA_ID"
#    - Polygon (Cheaper): "https://polygon-rpc.com"
#    - Base (Coinbase Chain): "https://mainnet.base.org"
RPC_URL = "YOUR_RPC_URL_HERE" 

# 2. Your Wallet Details
CHAIN_ID = 1  # 1 for Ethereum, 137 for Polygon, 8453 for Base
MY_ADDRESS = "0x3e1C8Fb332374483b0E5C4247281c9B2C4A9F39B"
# EXPORT your private key to your terminal first: export PVT_KEY='your_key'
# We read it from env for security. DO NOT PASTE IT HERE.
PRIVATE_KEY = os.getenv('PVT_KEY') 

def launch_sequence():
    print("🚀 INITIALIZING MAINNET LAUNCH SEQUENCE...")
    
    if not PRIVATE_KEY:
        print("   [!] CRITICAL ERROR: Private Key not found.")
        print("   Run this in terminal first: export PVT_KEY='your_actual_private_key'")
        return

    # 1. Connect to Blockchain
    print("   [1/5] Connecting to Mainnet Node...")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("   [!] Connection Failed. Check your RPC URL.")
        return
    print(f"   [OK] Connected. Latency: {w3.eth.get_block('latest').number} blocks")

    # 2. Compile Contract (Just-in-Time)
    print("   [2/5] Compiling 'Zero-Kelvin' Solidity Code...")
    install_solc('0.8.20')
    
    with open("./Finux/contracts/FrostEther.sol", "r") as file:
        frost_source = file.read()

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {"FrostEther.sol": {"content": frost_source}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}}
    })
    
    # Extract ABI and Bytecode
    bytecode = compiled_sol["contracts"]["FrostEther.sol"]["FrostEther"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["FrostEther.sol"]["FrostEther"]["abi"]

    # 3. Build Transaction
    print("   [3/5] Constructing Genesis Transaction...")
    FrostContract = w3.eth.contract(abi=abi, bytecode=bytecode)
    
    # Get nonce
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    
    # Estimate Gas (Safety Check)
    # This ensures we don't spend too much
    gas_estimate = FrostContract.constructor().estimate_gas({'from': MY_ADDRESS})
    print(f"   [i] Estimated Gas Cost: {gas_estimate} units")
    
    transaction = FrostContract.constructor().build_transaction({
        "chainId": CHAIN_ID,
        "gasPrice": w3.eth.gas_price,
        "from": MY_ADDRESS,
        "nonce": nonce
    })

    # 4. Sign & Send
    print("   [4/5] SIGNING TRANSACTION (Irreversible)...")
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    
    print("   [>>] BROADCASTING TO NETWORK...")
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"   [TX] Hash: {tx_hash.hex()}")

    # 5. Wait for Receipt
    print("   [5/5] Waiting for Block Confirmation...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print("\n✅ LAUNCH SUCCESSFUL.")
    print(f"   ❄️  CONTRACT ADDRESS: {tx_receipt.contractAddress}")
    print("   (Save this address. This is the permanent home of FSZT.)")
    
    # Save address to file for the App to use
    with open("fszt_address.txt", "w") as f:
        f.write(tx_receipt.contractAddress)

if __name__ == "__main__":
    launch_sequence()
