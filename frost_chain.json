import json
import time
import hashlib

# --- CONFIGURATION ---
GENESIS_TARGET = "0x5147f68049bdf47fcb778c89544f9f7d1ed7da1d"
TOTAL_SUPPLY = 100_000_000.00  # 100 Million FNR
NETWORK_NAME = "Frost Protocol Mainnet"

def calculate_hash(block):
    """Creates a SHA-256 hash of a block."""
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def create_genesis():
    print(f"[❄️] Initializing {NETWORK_NAME}...")
    print(f"[i] Minting {TOTAL_SUPPLY:,.2f} FNR to Cold Storage...")
    print(f"[i] Target: {GENESIS_TARGET}")

    timestamp = time.time()
    
    # The "God Transaction" that creates the coins
    genesis_transaction = {
        "sender": "0x0000000000000000000000000000000000000000", # Null address
        "recipient": GENESIS_TARGET,
        "amount": TOTAL_SUPPLY,
        "note": "Genesis Allocation / Cold Storage"
    }

    # Block 0 Structure
    genesis_block = {
        "index": 1,
        "timestamp": timestamp,
        "transactions": [genesis_transaction],
        "proof": 100, # Arbitrary genesis proof
        "previous_hash": "0" # No previous block
    }

    # Hash the genesis block to seal it
    block_hash = calculate_hash(genesis_block)
    
    # The Chain Data Structure
    chain_data = {
        "network": NETWORK_NAME,
        "version": "1.0 (Iceland)",
        "genesis_time": timestamp,
        "chain": [genesis_block],
        "latest_hash": block_hash
    }

    # Save to file
    filename = "frost_chain.json"
    with open(filename, "w") as f:
        json.dump(chain_data, f, indent=4)

    print("-" * 50)
    print(f"[✅] GENESIS BLOCK FORGED.")
    print(f"[📄] Ledger saved to: {filename}")
    print(f"[🔒] Supply Locked. The network is now live.")
    print("-" * 50)

if __name__ == "__main__":
    create_genesis()
