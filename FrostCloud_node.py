from flask import Flask, request, jsonify
import time
import hashlib
import json
import uuid

app = Flask(__name__)

# --- Configuration ---
NODE_VERSION = "FrostCloud-v1.2 (Iceland)"
MASTER_KEY = "frost_admin_8492"  # Change this for production
LEDGER_FILE = "frost_ledger.json"

# --- In-Memory Storage (Replace with Redis/SQL for production) ---
connected_devices = {}
transaction_pool = []

# --- Blockchain / Protocol Logic ---

class FrostChain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': transaction_pool.copy(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        transaction_pool.clear()
        self.chain.append(block)
        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

frost_net = FrostChain()

# --- API Endpoints ---

@app.route('/status', methods=['GET'])
def get_status():
    """Health check for the node."""
    return jsonify({
        'node': 'Active',
        'version': NODE_VERSION,
        'connected_devices': len(connected_devices),
        'chain_length': len(frost_net.chain)
    }), 200

@app.route('/device/handshake', methods=['POST'])
def register_device():
    """Registers a Finux or FrostGlass device."""
    data = request.get_json()
    device_id = data.get('device_id')
    device_type = data.get('type', 'Unknown')
    
    if not device_id:
        return jsonify({'error': 'Missing device_id'}), 400

    session_token = str(uuid.uuid4())
    connected_devices[device_id] = {
        'type': device_type,
        'last_seen': time.time(),
        'session': session_token
    }
    
    print(f"[☁️] New Connection: {device_type} ({device_id})")
    
    return jsonify({
        'message': 'Handshake successful',
        'session_token': session_token,
        'config': {
            'sync_interval': 60,
            'ota_channel': 'stable'
        }
    }), 201

@app.route('/protocol/transaction', methods=['POST'])
def new_transaction():
    """Adds a new transaction to the Frost Protocol."""
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    
    if not all(k in values for k in required):
        return jsonify({'message': 'Missing values'}), 400

    # Add to pool
    transaction_pool.append({
        'sender': values['sender'],
        'recipient': values['recipient'],
        'amount': values['amount'],
        'signature': 'valid' # Placeholder for crypto sig check
    })
    
    response = {'message': f'Transaction will be added to Block {len(frost_net.chain) + 1}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    """Returns the full blockchain data."""
    response = {
        'chain': frost_net.chain,
        'length': len(frost_net.chain),
    }
    return jsonify(response), 200

# --- Mine Block (Simulation) ---
@app.route('/mine', methods=['GET'])
def mine():
    """Simulates mining a block to confirm transactions."""
    last_block = frost_net.chain[-1]
    # Simple Proof of Work simulation
    proof = last_block['proof'] + 1 
    previous_hash = frost_net.hash(last_block)
    block = frost_net.create_block(proof, previous_hash)
    
    response = {
        'message': 'New Block Forged',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

if __name__ == '__main__':
    print(f"[❄️] FrostCloud Node Initializing...")
    print(f"[i] Listening on 0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
