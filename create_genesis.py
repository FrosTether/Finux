import hashlib
import json
import time

def generate_genesis_block():
    # Genesis Metadata
    genesis_data = {
        "index": 0,
        "timestamp": 1737633120, # Jan 23, 2026
        "data": "Genesis Block: FrosTether Network - Established by Jacob Frost",
        "previous_hash": "0", # No prior block exists
        "nonce": 23
    }
    
    # Calculate unique Genesis Hash
    block_string = json.dumps(genesis_data, sort_keys=True).encode()
    genesis_hash = hashlib.sha256(block_string).hexdigest()
    
    genesis_data["hash"] = genesis_hash
    
    print("❄️  Genesis Block Created Successfully!")
    print(json.dumps(genesis_data, indent=4))
    
    # Save to file
    with open('genesis_block.json', 'w') as f:
        json.dump(genesis_data, f, indent=4)

if __name__ == "__main__":
    generate_genesis_block()
