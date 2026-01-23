import json
import os
from web3 import Web3
from solcx import compile_standard, install_solc

# --- CONFIGURATION ---
# 1. RPC URL (Base Mainnet or Testnet)
RPC_URL = "https://mainnet.base.org"  # Change to Sepolia/Testnet if testing
# 2. Your Wallet (The Deployer)
MY_ADDRESS = "YOUR_WALLET_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY" # ⚠️ Never share this!
# 3. Contract Arguments
FROST_TOKEN_ADDRESS = "0x..." # Address of the FSC Token Contract
WILLIAMS_ADDRESS = "0x..."    # The address you find for Williams.base.eth

# --- SETUP ---
print("Installing Solidity Compiler...")
install_solc("0.8.0")

# Read the Solidity file
with open("./FrostGovernance.sol", "r") as file:
    governance_file = file.read()

# Compile the Contract
print("Compiling Contract...")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"FrostGovernance.sol": {"content": governance_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

bytecode = compiled_sol["contracts"]["FrostGovernance.sol"]["FrostGovernance"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["FrostGovernance.sol"]["FrostGovernance"]["abi"]

# Connect to Blockchain
w3 = Web3(Web3.HTTPProvider(RPC_URL))
chain_id = w3.eth.chain_id

print(f"Connected to chain ID: {chain_id}")

# --- DEPLOYMENT ---
print("Deploying Contract...")
FrostGovernance = w3.eth.contract(abi=abi, bytecode=bytecode)

# Build the transaction
nonce = w3.eth.get_transaction_count(MY_ADDRESS)
transaction = FrostGovernance.constructor(
    FROST_TOKEN_ADDRESS, 
    WILLIAMS_ADDRESS
).build_transaction({
    "chainId": chain_id,
    "gasPrice": w3.eth.gas_price,
    "from": MY_ADDRESS,
    "nonce": nonce,
})

# Sign the transaction
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

# Send the transaction
print("Sending transaction...")
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(f"Transaction sent! Hash: {w3.to_hex(tx_hash)}")

# Wait for receipt
print("Waiting for confirmation...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("--------------------------------------------------")
print(f"✅ Contract Deployed Successfully!")
print(f"📍 Contract Address: {tx_receipt.contractAddress}")
print("--------------------------------------------------")

# Save the Address and ABI for future use
data = {
    "address": tx_receipt.contractAddress,
    "abi": abi
}
with open("contract_data.json", "w") as outfile:
    json.dump(data, outfile)
print("Contract data saved to contract_data.json")
