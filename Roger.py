import time
import requests
from web3 import Web3

# --- CONFIGURATION ---
DOGE_VAULT_ADDR = "DJTDVRxJGtcuSsxwT7GHbkdCabqaTa1C7s"
BASE_RPC_URL = "https://mainnet.base.org"
CONTRACT_ADDRESS = "0xYourFrostContractAddressHere"
PRIVATE_KEY = "YOUR_ORACLE_WALLET_PRIVATE_KEY"

# Doge API (Using SoChain for demo, can use BlockCypher for prod)
DOGE_API_URL = f"https://sochain.com/api/v2/get_tx_received/DOGE/{DOGE_VAULT_ADDR}"

# --- SETUP ---
w3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

# Simple database of linked users (In prod, use a real DB or read from contract)
# Format: {'doge_address': 'base_0x_address'}
LINKED_IDENTITIES = {
    'D8v...exampleDoge': '0x123...exampleBase'
}

def get_mirrored_address(doge_addr):
    """
    If no Base identity is found, derive a 'Mirrored' address.
    Simple strategy: Hash the Doge address to create a deterministic EVM address.
    """
    # This creates a unique 0x address based on the Doge string
    addr_hash = w3.keccak(text=doge_addr)
    # Take last 20 bytes to make it an address
    mirrored = w3.to_checksum_address(addr_hash[-20:])
    return mirrored

def process_mint(doge_tx):
    sender = doge_tx['inputs'][0]['address'] # Simplified parsing
    amount_doge = float(doge_tx['value']) # Value in DOGE
    tx_hash = doge_tx['txid']
    
    # 1. DETERMINE RECIPIENT
    if sender in LINKED_IDENTITIES:
        recipient = LINKED_IDENTITIES[sender]
        print(f"✅ Found Linked Identity: {recipient}")
    else:
        recipient = get_mirrored_address(sender)
        print(f"🪞 No Link. Using Mirrored Address: {recipient}")

    # 2. CONVERT TO WEI/SATOSHI INTEGERS
    # Assuming the contract expects the raw integer input of Doge (no decimals logic in py)
    # But usually Doge is 8 decimals, standard ERC20 is 18.
    # The Solidity math we wrote assumes inputs are proportional. 
    # Let's send the raw Doge units (Sats).
    
    amount_sats = int(amount_doge * 100_000_000) # Doge has 8 decimals

    # 3. CALL SMART CONTRACT
    contract_abi = [
        # ... (Include your ABI for mintFromDoge here) ...
        {
            "inputs": [
                {"internalType": "address", "name": "recipient", "type": "address"},
                {"internalType": "uint256", "name": "dogeAmount", "type": "uint256"}
            ],
            "name": "mintFromDoge",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
    
    contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
    
    # Build Transaction
    tx = contract.functions.mintFromDoge(
        recipient,
        amount_sats
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })
    
    # Sign & Send
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"❄️ Minted FRST for {amount_doge} DOGE. TX: {w3.to_hex(tx_hash)}")

def poll_doge_vault():
    print("👀 Watching Doge Vault...")
    # In production, keep track of last_processed_block to avoid duplicates
    last_txs = set()
    
    while True:
        try:
            response = requests.get(DOGE_API_URL).json()
            txs = response['data']['txs']
            
            for tx in txs:
                if tx['txid'] not in last_txs:
                    print(f"🚀 New Doge Deposit Detected: {tx['txid']}")
                    process_mint(tx)
                    last_txs.add(tx['txid'])
            
            time.sleep(30) # Check every 30 seconds
            
        except Exception as e:
            print(f"Error polling: {e}")
            time.sleep(30)

if __name__ == "__main__":
    poll_doge_vault()
