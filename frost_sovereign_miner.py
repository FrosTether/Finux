#!/usr/bin/env python3
"""
FROST SOVEREIGN MINER (v2.0 - ♊ EDITION)
------------------------------------------------
Kernel: Finux (BSD)
Consensus: Proof-of-Crush (Active Session)
Economics: 13.37/2 Base | 5y 8m Halving
Security: Air-Gapped Key Signing (Jail-Based)
"""

import json
import time
import os
import math
from datetime import datetime
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv

# --- 1. SECURITY CONFIGURATION ---
# Load the Private Key from the secure, hidden .env file
# Location: /usr/jails/frost_crush/root/.env
ENV_PATH = "/root/.env"
load_dotenv(ENV_PATH)

PRIVATE_KEY = os.getenv("FINUX_PRIVATE_KEY")
REGISTRY_PATH = "/etc/finux/registry.json"
GAME_LOG_PATH = "/var/log/frost_crush/activity.log"

# --- 2. ♊ FROST ECONOMICS ♊ ---
GENESIS_DATE = datetime(2025, 12, 1)  # Protocol Launch
BASE_REWARD = 6.685                   # 13.37 / 2
HALVING_MONTHS = 68                   # 5 Years, 8 Months
BLOCK_TIME = 150                      # Seconds

# --- 3. NETWORK CONFIGURATION ---
RPC_URL = "https://mainnet.base.org"
CHAIN_ID = 8453

class FrostSovereignMiner:
    def __init__(self):
        self._check_security()
        
        # Initialize Web3 Connection
        self.w3 = Web3(Web3.HTTPProvider(RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        if not self.w3.is_connected():
            print("[!] FATAL: Cannot connect to Base Mainnet.")
            exit(1)

        # Load Keys & Ecosystem
        self.account = self.w3.eth.account.from_key(PRIVATE_KEY)
        self.registry = self._load_registry()
        
        # Contract Setup
        self.ftc_address = self.registry['contracts']['FTC']['address']
        self.owner_ens = self.registry['ecosystem']['owner_ens']
        
        # Minimal ABI for the 'mint' function
        self.mint_abi = '[{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
        self.contract = self.w3.eth.contract(address=self.ftc_address, abi=self.mint_abi)

        # Session State
        self.current_streak = 0
        self.last_log_check = time.time()

        print(f"[*] ------------------------------------------------")
        print(f"[*] FROST SOVEREIGN MINER ♊ ONLINE")
        print(f"[*] Node: {self.account.address[:6]}...{self.account.address[-4:]}")
        print(f"[*] Target: {self.ftc_address}")
        print(f"[*] Halving Schedule: {HALVING_MONTHS} Months")
        print(f"[*] ------------------------------------------------")

    def _check_security(self):
        """Ensures we have the keys to the castle."""
        if not PRIVATE_KEY:
            print("[!] FATAL: FINUX_PRIVATE_KEY not found in .env")
            exit(1)
        if not os.path.exists(REGISTRY_PATH):
            print(f"[!] FATAL: Registry missing at {REGISTRY_PATH}")
            exit(1)

    def _load_registry(self):
        with open(REGISTRY_PATH, 'r') as f:
            return json.load(f)

    def calculate_current_reward(self):
        """
        Implements the ♊ Halving Logic.
        Returns the exact amount of FTC to mint for this block.
        """
        now = datetime.now()
        diff = now - GENESIS_DATE
        months_passed = diff.days / 30.44 
        
        halvings = int(months_passed // HALVING_MONTHS)
        current_reward = BASE_REWARD / (2 ** halvings)
        
        return current_reward, halvings

    def check_proof_of_crush(self):
        """
        The Watchdog: Checks if the game is active.
        """
        try:
            # In production, check file modification time or parse last line
            # For this script, we assume file updates = active play
            if not os.path.exists(GAME_LOG_PATH):
                return False
                
            mtime = os.path.getmtime(GAME_LOG_PATH)
            if (time.time() - mtime) < 10: # Active in last 10s
                return True
            return False
        except Exception:
            return False

    def execute_mint(self):
        """
        Signs and broadcasts the transaction.
        """
        reward_amount, era = self.calculate_current_reward()
        wei_amount = self.w3.to_wei(reward_amount, 'ether')
        
        # Resolve recipient (Using hardcoded address for safety if ENS fails)
        # Replace this with your actual public address if ENS resolution is not set up in script
        recipient = "0xYourPublicAddressHere" 

        print(f"\n[>] MINING BLOCK... (Reward: {reward_amount:.4f} FTC | Era: {era})")

        try:
            # 1. Build
            nonce = self.w3.eth.get_transaction_count(self.account.address)
            tx = self.contract.functions.mint(recipient, wei_amount).build_transaction({
                'chainId': CHAIN_ID,
                'gas': 200000,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': nonce,
            })

            # 2. Sign (The Sovereign Step)
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

            # 3. Broadcast
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
            print(f"[SUCCESS] Block Confirmed. Hash: {self.w3.to_hex(tx_hash)}")
            
        except Exception as e:
            print(f"[!] MINT FAILED: {str(e)}")

    def run(self):
        """Main Loop"""
        print("[*] Monitoring Proof-of-Crush...")
        
        while True:
            if self.check_proof_of_crush():
                self.current_streak += 1
                
                # Visual Feedback
                if self.current_streak % 10 == 0:
                    print(f"    > Mining Progress: {self.current_streak}/{BLOCK_TIME}")

                # Block Found?
                if self.current_streak >= BLOCK_TIME:
                    self.execute_mint()
                    self.current_streak = 0 # Reset for next block
            else:
                if self.current_streak > 0:
                    print("[!] Session Idle. Streak Broken.")
                    self.current_streak = 0
            
            time.sleep(1)

if __name__ == "__main__":
    # Create dummy log for testing if it doesn't exist
    if not os.path.exists(GAME_LOG_PATH):
        os.makedirs(os.path.dirname(GAME_LOG_PATH), exist_ok=True)
        with open(GAME_LOG_PATH, 'w') as f:
            f.write("INIT_SESSION")

    miner = FrostSovereignMiner()
    miner.run()
