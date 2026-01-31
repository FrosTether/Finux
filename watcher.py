# In process_mint function, after calculating amount_sats

# Now using 3 * pi multiplier instead of 3.1337
print(f"❄️ Pi Freeze: {amount_doge} DOGE → ~{amount_doge * 9.4248:.2f} FRST (exact calc in contract)")

# The rest stays the same — contract handles the precise math
import time
import requests
from web3 import Web3

# --- CONFIGURATION ---
DOGE_VAULT_ADDR = "DJTDVRxJGtcuSsxwT7GHbkdCabqaTa1C7s"
BASE_RPC_URL = "https://mainnet.base.org"  # Or sepolia.base.org for test
CONTRACT_ADDRESS = "0xYourDeployedFrostContractAddressHere"
PRIVATE_KEY = "0xYourOraclePrivateKeyHere"  # USE ENV VAR IN PROD!

# Doge API (SoChain for MVP; upgrade to BlockCypher or own node)
DOGE_API_URL = f"https://sochain.com/api/v2/get_tx_received/DOGE/{DOGE_VAULT_ADDR}"

# --- SETUP ---
w3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

# Mock DB for linked identities (use real DB like PostgreSQL in prod)
LINKED_IDENTITIES = {}  # e.g., {'DogeAddr': '0xBaseAddr'}

def get_mirrored_address(doge_addr):
    addr_hash = w3.keccak(text=doge_addr)
    return w3.to_checksum_address(addr_hash[-20:])

def process_mint(doge_tx):
    sender = doge_tx.get('inputs', [{}])[0].get('address')  # Improved parsing
    amount_doge = float(doge_tx.get('value', 0))
    if amount_doge <= 0:
        return  # Skip invalid

    tx_hash = doge_tx['txid']
    
    recipient = LINKED_IDENTITIES.get(sender) or get_mirrored_address(sender)
    print(f"✅ Recipient: {recipient} (Linked: {bool(LINKED_IDENTITIES.get(sender))})")

    amount_sats = int(amount_doge * 100_000_000)  # To satoshis

    # ABI snippet for mintFromDoge
    contract_abi = [
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
    
    tx = contract.functions.mintFromDoge(recipient, amount_sats).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200_000,
        'gasPrice': w3.eth.gas_price * 2  # Bump for priority
    })
    
    signed_tx = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"❄️ π-Perfected Mint: {amount_doge} DOGE → ~{amount_doge * 3.14159:.2f} FRST. TX: {w3.to_hex(tx_hash)}")

def poll_doge_vault():
    print("👀 Watching Doge Vault for Pi Freezes...")
    last_txs = set()  # Persist to file/DB in prod
    
    while True:
        try:
            response = requests.get(DOGE_API_URL).json()
            txs = response.get('data', {}).get('txs', [])
            
            for tx in txs:
                if tx['txid'] not in last_txs and tx.get('confirmations', 0) >= 6:  # Wait for confs
                    print(f"🚀 New Deposit: {tx['txid']}")
                    process_mint(tx)
                    last_txs.add(tx['txid'])
            
            time.sleep(30)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    poll_doge_vault()