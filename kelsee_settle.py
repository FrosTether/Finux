import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Bridge Configuration
WALLET_RPC_URL = "http://127.0.0.1:18082/json_rpc"

def execute_settlement(amount_xmr, destination_address):
    print(f"🔱 [SETTLEMENT] Initiating transfer for G-Partner: {os.getenv('G_PARTNER_NAME')}...")
    
    # Convert XMR to Atomic Units (10^12)
    atomic_amount = int(amount_xmr * 1e12)
    
    payload = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": "transfer",
        "params": {
            "destinations": [{"amount": atomic_amount, "address": destination_address}],
            "account_index": 0,
            "priority": 1, # Flash settlement speed
            "ring_size": 11, # Monokiller anonymity level
            "get_tx_key": True
        }
    }

    try:
        response = requests.post(WALLET_RPC_URL, data=json.dumps(payload), timeout=30).json()
        if "result" in response:
            tx_hash = response['result']['tx_hash']
            print(f"✅ SUCCESS: Settlement deployed to Monokiller Ledger.")
            print(f"🔗 TX Hash: {tx_hash}")
            print(f"💰 Destination Bridge: {os.getenv('VENMO_BRIDGE_ID')} (@drfrostwavhz)")
        else:
            print(f"❌ ERROR: {response.get('error', {}).get('message', 'Unknown Protocol Error')}")
    except Exception as e:
        print(f"❌ CRITICAL: Could not reach Frostnerjo Bridge. Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 kelsee_settle.py [Amount_XMR] [Bridge_Address]")
    else:
        execute_settlement(float(sys.argv[1]), sys.argv[2])
