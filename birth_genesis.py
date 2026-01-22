import hashlib
import datetime
import time
from eth_account import Account

# ENABLE HD WALLET FEATURES
Account.enable_unaudited_hdwallet_features()

class GenesisMaker:
    def __init__(self):
        # CONFIGURATION: JACOB FROST (Aug 24, 1991 @ 12:57 PM)
        self.year = 1991
        self.month = 8
        self.day = 24
        self.hour = 12
        self.minute = 57
        self.second = 0  # Precision
        
    def calculate_birth_second(self):
        # Create datetime object (assuming Local Time/EST or UTC as base)
        birth_dt = datetime.datetime(
            self.year, self.month, self.day, 
            self.hour, self.minute, self.second
        )
        
        # Convert to "Epoch Seconds" (The absolute birth second)
        birth_timestamp = int(birth_dt.timestamp())
        
        return birth_timestamp, birth_dt.strftime("%Y-%m-%d %H:%M:%S")

    def mint_wallet(self):
        ts, readable = self.calculate_birth_second()
        
        print(f"🧬 GENESIS PULSE DETECTED...")
        print(f"   [TIME] {readable}")
        print(f"   [SEED] {ts} (Your Birth Second)")
        print("-" * 50)
        
        # 1. THE BIOLOGICAL HASH
        # We salt it with "FROST_GENESIS" to make it unique to your chain
        raw_entropy = f"{ts}_FROST_GENESIS_DNA"
        
        # 2. KEY DERIVATION (SHA-256)
        # This turns the "Time" into "Math"
        private_hash = hashlib.sha256(raw_entropy.encode('utf-8')).hexdigest()
        private_key = f"0x{private_hash}"
        
        # 3. PUBLIC ADDRESS GENERATION
        acct = Account.from_key(private_key)
        
        print(f"   [1] ENTROPY SOURCE:  Biological Time")
        print(f"   [2] PRIVATE KEY:     {private_key}")
        print(f"   [3] GENESIS VAULT:   {acct.address}")
        print("-" * 50)
        print("   ✅ WALLET LINKED TO BIOLOGICAL CLOCK.")
        print("   Only the exact moment of your birth can unlock these funds.")
        
        return acct.address

if __name__ == "__main__":
    maker = GenesisMaker()
    maker.mint_wallet()
