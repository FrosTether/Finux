import json
import time
import hashlib
from flask import jsonify

# --- FROST PROTOCOL: SMART CONTRACT REGISTRY ---
# The immutable addresses for the Frost Ecosystem
CONTRACTS = {
    "$FROST":    "0xc34a134b37e97e949a56461960d4cf5361ae832b",
    "FTC":       "0xee132a0fa1f0724d3ec3936f0cdc5213af748c42",
    "FROSTCOIN": "0x6a5c9062648db45b0ff92b8d9b86cd755452a571",
    "FNR":       "0xe3a50d4b636274b462f4be5f715a14a6a42e242d",  # <--- REWARD TOKEN
    "FETH":      "0xec9cf89a9829cc6d7aea06d5fc33ae23746076c8",
    "FsZT":      "0x815447cdcf1714b73d01db46955ee0e11195e63c",
    "OTHERS":    "0x52f260614c434ec3aefab821ae7b63e5272c5b36"
}

# --- CONFIGURATION ---
# Conversion: 1000 Game Points = 1.5 FNR
REWARD_TOKEN = "FNR"
CONVERSION_RATE = 0.0015 

# --- MOCK LEDGER (Simulating Google Firestore) ---
# In production, replace this dict with a connection to Firestore or SQL
user_ledger = {
    "JacobFrost": {"balance": 5000.00, "wallet": "0xJacobMainWallet"},
    "TestUser":   {"balance": 0.00,    "wallet": "0xTestWallet123"}
}

def sync_score(request):
    """
    The Google Cloud Function Entry Point.
    Receives Game Data -> Calculates FNR -> 'Mints' Tokens.
    """
    
    # 1. CORS Headers (Allows the Android App to talk to this Server)
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    # 2. Parse Incoming Data
    request_json = request.get_json(silent=True)
    
    if not request_json or 'user_id' not in request_json or 'score' not in request_json:
        return (jsonify({"error": "Invalid Data Payload"}), 400, headers)

    user_id = request_json['user_id']
    game_score = int(request_json['score'])
    
    # 3. Calculate FNR Rewards
    tokens_earned = game_score * CONVERSION_RATE
    target_contract = CONTRACTS[REWARD_TOKEN]

    print(f"❄️ [FROST ORACLE] Incoming Sync: User {user_id} | Score {game_score}")
    print(f"❄️ [FROST ORACLE] Target Contract: {target_contract} ({REWARD_TOKEN})")

    # 4. Execute Smart Contract Interaction (Simulation)
    tx_hash = execute_mint_transaction(user_id, tokens_earned, target_contract)

    # 5. Update Internal Ledger
    if user_id not in user_ledger:
        user_ledger[user_id] = {"balance": 0.00, "wallet": "0xNewWallet"}
    
    user_ledger[user_id]['balance'] += tokens_earned
    new_balance = user_ledger[user_id]['balance']

    # 6. Response to App
    response_data = {
        "status": "success",
        "reward_token": REWARD_TOKEN,
        "contract": target_contract,
        "tokens_minted": tokens_earned,
        "new_balance": new_balance,
        "tx_hash": tx_hash,
        "message": f"Successfully mined {tokens_earned:.4f} {REWARD_TOKEN}"
    }

    return (jsonify(response_data), 200, headers)

def execute_mint_transaction(user_id, amount, contract_address):
    """
    Simulates the Web3 'mint' call to the specific Frost Protocol contract.
    """
    # In a live Web3 version, this is where we would use web3.py to sign a transaction
    # using the Owner Private Key and send it to the Polygon/ETH RPC.
    
    print(f"⛓️  [BLOCKCHAIN] Calling Smart Contract: {contract_address}")
    print(f"⛓️  [BLOCKCHAIN] Function: mint(to={user_id}, amount={amount})")
    
    # Simulate Network Latency
    time.sleep(0.5) 
    
    # Generate a fake Transaction Hash that looks like a real Ethereum Tx
    simulated_hash = "0x" + hashlib.sha256(f"{user_id}{amount}{time.time()}".encode()).hexdigest()
    
    print(f"✅ [BLOCKCHAIN] Transaction Confirmed: {simulated_hash}")
    return simulated_hash
