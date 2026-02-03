#!/usr/bin/env python3
import json
import time
import os
from web3 import Web3
from dotenv import load_dotenv

# --- SECURITY: LOAD SECRETS FROM ENVIRONMENT ---
# Create a .env file in your Jail: /usr/jails/frost_crush/root/.env
# Content: FINUX_PRIVATE_KEY=0xYourActualPrivateKeyHere
load_dotenv("/root/.env") 

PRIVATE_KEY = os.getenv("FINUX_PRIVATE_KEY")
if not PRIVATE_KEY:
    print("[!] FATAL: No Private Key found. Mining disabled.")
    exit(1)

# --- CONFIGURATION ---
RPC_URL = "https://mainnet.base.org"
CHAIN_ID = 8453
REGISTRY_PATH = "/etc/finux/registry.json"

class SovereignMiner:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(RPC_URL))
        self.account = self.w3.eth.account.from_key(PRIVATE_KEY)
        self.data = self._load_registry()
        
        # Contract Setup
        self.ftc_address = self.data['contracts']['FTC']['address']
        # Minimal ABI for Minting
        self.mint_abi = '[{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
        self.contract = self.w3.eth.contract(address=self.ftc_address, abi=self.mint_abi)

        print(f"[*] FINUX SOVEREIGN SIGNER ONLINE")
        print(f"[*] Node Address: {self.account.address}")
        print(f"[*] Target Contract: {self.ftc_address}")

    def _load_registry(self):
        with open(REGISTRY_PATH, 'r') as f:
            return json.load(f)

    def execute_mint(self):
        """
        Signs and broadcasts the mint transaction from the Secure Jail.
        JavaScript cannot touch this.
        """
        target_wallet = self.data['ecosystem']['owner_ens']
        # Resolve ENS if needed, or hardcode the hex address from registry
        # For safety, we use the hex owner address directly if stored, or self.account
        recipient = "0xYourWalletAddressHere" 
        amount = self.w3.to_wei(10, 'ether') # Reward: 10 FTC

        print(f"[>] Initiating Mint Sequence...")
        
        # 1. Build Transaction
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        tx = self.contract.functions.mint(recipient, amount).build_transaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })

        # 2. Sign with Local Key (Air-Gapped from Web)
        signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

        # 3. Broadcast
        try:
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f"[SUCCESS] Minted 10 FTC. Hash: {self.w3.to_hex(tx_hash)}")
        except Exception as e:
            print(f"[!] TRANSACTION FAILED: {str(e)}")

    def run(self):
        print("[*] Monitoring Proof-of-Crush Logs...")
        # (Insert Watchdog Logic Here - simplified for brevity)
        while True:
            # if check_logs_for_win():
            #    self.execute_mint()
            time.sleep(10)

if __name__ == "__main__":
    miner = SovereignMiner()
    # miner.execute_mint() # Uncomment to test one transaction
    miner.run()
