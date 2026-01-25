import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration from .env
RPC_HOST = "127.0.0.1"
DAEMON_PORT = 18081  # Monero Daemon
WALLET_PORT = 18082  # Frostnerjo Wallet RPC

def rpc_call(port, method, params=None):
    url = f"http://{RPC_HOST}:{port}/json_rpc"
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": method,
        "params": params or {}
    }
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return response.json().get('result', {})
    except:
        return None

def display_dashboard():
    print(f"--- ♍ VIRGO x1777 | G-PARTNER DASHBOARD ---")
    print(f"Overseer: {os.getenv('G_PARTNER_NAME', 'Kelsee Missler')}")
    print("---")

    # 1. Check Node Sync Status
    node_info = rpc_call(DAEMON_PORT, "get_info")
    if node_info:
        sync_pct = (node_info['height'] / node_info['target_height'] * 100) if node_info.get('target_height') else 100
        status = "✅ SYNCED" if node_info.get('synchronized') else f"⏳ SYNCING ({sync_pct:.2f}%)"
        print(f"Network Status:  {status}")
        print(f"Throughput:      FOSS x{os.getenv('NETWORK_MULTIPLIER', '25')}")
    else:
        print("Network Status:  ❌ OFFLINE (Check Monero Daemon)")

    # 2. Check Wallet & Liquidity
    wallet_info = rpc_call(WALLET_PORT, "get_balance", {"account_index": 0})
    if wallet_info:
        # Monero uses 12 atomic units per 1 XMR
        balance = wallet_info.get('balance', 0) / 1e12
        unlocked = wallet_info.get('unlocked_balance', 0) / 1e12
        
        print(f"Vault Balance:   {balance:.4f} XMR")
        print(f"Unlocked:        {unlocked:.4f} XMR")
        print(f"G-Partner Limit: ${os.getenv('SETTLEMENT_ALLOCATION', '50,000')}")
        print(f"Bridge Active:   🖇️ {os.getenv('VENMO_BRIDGE_ID', '@drfrostwavhz')}")
    else:
        print("Wallet Status:   ❌ LOCKED (Awaiting 1-of-3 Signature)")

    print("---")
    print("Security Layer:  MONOKILLER ALPHA")

if __name__ == "__main__":
    display_dashboard()
