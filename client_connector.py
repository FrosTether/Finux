import requests
import json
import uuid
import time
import platform

class FrostLink:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url
        self.device_id = str(uuid.getnode()) # Generates unique ID based on hardware address
        self.session_token = None
        self.device_type = f"Finux-{platform.system()}"
        self.is_connected = False

    def handshake(self):
        """Registers this device with the FrostCloud Node."""
        endpoint = f"{self.server_url}/device/handshake"
        payload = {
            "device_id": self.device_id,
            "type": self.device_type
        }

        try:
            print(f"[❄️] Attempting handshake with {self.server_url}...")
            response = requests.post(endpoint, json=payload, timeout=5)
            
            if response.status_code == 201:
                data = response.json()
                self.session_token = data.get('session_token')
                self.is_connected = True
                print(f"[✅] Connected! Session: {self.session_token[:8]}...")
                return True
            else:
                print(f"[X] Handshake refused: {response.text}")
                return False

        except requests.exceptions.ConnectionError:
            print(f"[!] Error: Could not reach FrostCloud Node at {self.server_url}")
            return False

    def send_transaction(self, recipient, amount):
        """Sends FNR tokens to another address."""
        if not self.is_connected:
            print("[!] Cannot transact: Offline")
            return

        endpoint = f"{self.server_url}/protocol/transaction"
        payload = {
            "sender": self.device_id,
            "recipient": recipient,
            "amount": amount
        }

        try:
            response = requests.post(endpoint, json=payload)
            if response.status_code == 201:
                print(f"[💸] Sent {amount} FNR to {recipient[:8]}...")
            else:
                print(f"[!] Transaction failed: {response.text}")
        except Exception as e:
            print(f"[!] Error sending transaction: {e}")

    def get_network_status(self):
        """Fetches the current block height and node status."""
        try:
            response = requests.get(f"{self.server_url}/status")
            if response.status_code == 200:
                return response.json()
        except:
            return None

# --- Usage Example ---
if __name__ == "__main__":
    # If testing locally, ensure FrostCloud_Node.py is running first
    client = FrostLink(server_url="http://127.0.0.1:5000")
    
    if client.handshake():
        # Check network status
        status = client.get_network_status()
        print(f"[i] Network Version: {status.get('version')}")
        print(f"[i] Current Block Height: {status.get('chain_length')}")

        # Simulate a test transaction
        time.sleep(1)
        client.send_transaction(recipient="wallet_kelsee_01", amount=50.0)
