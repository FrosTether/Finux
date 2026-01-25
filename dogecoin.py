import json
import requests

# Configuration
RPC_USER = 'your_username'
RPC_PASSWORD = 'your_password'
RPC_PORT = 22555
RPC_URL = f"http://{RPC_USER}:{RPC_PASSWORD}@127.0.0.1:{RPC_PORT}"

def send_doge(address, amount):
    payload = {
        "method": "sendtoaddress",
        "params": [address, amount],
        "jsonrpc": "2.0",
        "id": 0,
    }
    
    try:
        response = requests.post(RPC_URL, json=payload).json()
        if response.get('error'):
            print(f"Error: {response['error']}")
        else:
            print(f"Transaction Success! TXID: {response['result']}")
    except Exception as e:
        print(f"Connection failed: {e}")

# Target data
target_address = "DSRmtBFDfV9Zb4QrzzrZ6uGi2KT6WsRPJz"
target_amount = 31337

send_doge(target_address, target_amount)
