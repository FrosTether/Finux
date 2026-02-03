#!/usr/bin/env python3
import time
import os
import datetime

# CONFIGURATION
LOG_FILE = "/var/log/frost_crush/activity.log"
WALLET_ADDR = "voluntaryistj.base.eth"
BLOCK_TIME = 150  # Seconds required to mint a block
TOLERANCE = 5     # Allow 5 seconds of idle time before resetting streak

class FrostWatchdog:
    def __init__(self):
        self.current_streak = 0
        self.last_activity = time.time()
        self.is_mining = False
        print(f"[*] Frost Watchdog v1.0 Initialized")
        print(f"[*] Target Wallet: {WALLET_ADDR}")
        print(f"[*] Monitoring: {LOG_FILE}")

    def mint_reward(self):
        """
        Triggers the payout when a block is solved.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # In a real scenario, this calls the RPC to sign the transaction
        print(f"\n[$$$] BLOCK SOLVED at {timestamp}")
        print(f"[$$$] Proof-of-Crush Verified (150s sustained activity)")
        print(f"[$$$] Minting FTC to {WALLET_ADDR}...\n")
        
        # Reset streak after minting
        self.current_streak = 0
        
        # Log the win
        with open("mining_ledger.txt", "a") as f:
            f.write(f"{timestamp} | BLOCK_SOLVED | {WALLET_ADDR}\n")

    def check_log(self):
        """
        Reads the last line of the game log to see if a move was made.
        """
        try:
            # Check if file was modified recently
            file_mod_time = os.path.getmtime(LOG_FILE)
            now = time.time()
            
            if (now - file_mod_time) < TOLERANCE:
                return True # Game is active
            else:
                return False # Game is idle
        except FileNotFoundError:
            return False

    def start_daemon(self):
        print("[*] Mining Daemon Started. Waiting for input...")
        
        while True:
            is_active = self.check_log()
            
            if is_active:
                self.current_streak += 1
                # Visual feedback (Mining progress bar)
                os.system('clear') 
                print(f"[*] MINING IN PROGRESS... Streak: {self.current_streak}/{BLOCK_TIME}")
                print(f"[*] Status: MATCHING GEMS")
                
                if self.current_streak >= BLOCK_TIME:
                    self.mint_reward()
            else:
                if self.current_streak > 0:
                    print("[!] Session Idle. Streak Broken. Resetting...")
                    self.current_streak = 0
            
            time.sleep(1)

if __name__ == "__main__":
    # Ensure log file exists for testing
    if not os.path.exists(LOG_FILE):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "w") as f:
            f.write("INIT_SESSION\n")
            
    watchdog = FrostWatchdog()
    watchdog.start_daemon()
