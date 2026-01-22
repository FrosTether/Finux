import hashlib
import datetime
from eth_account import Account

# ENABLE HD WALLET FEATURES
Account.enable_unaudited_hdwallet_features()

# CONFIGURATION: YOUR BIRTH DETAILS
BIRTH_MONTH = 8   # August
BIRTH_DAY = 24    # 24th
BIRTH_TIME = "12:57:00" # 12:57 PM
MILESTONES = [3, 15, 18, 21, 25, 29, 33]
BASE_YEAR = 1991

def get_timestamp(year):
    # Create date string: "YYYY-08-24 12:57:00"
    date_str = f"{year}-{BIRTH_MONTH:02d}-{BIRTH_DAY:02d} {BIRTH_TIME}"
    # Convert to datetime object
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    # Return UNIX timestamp (Integers)
    return int(dt.timestamp()), date_str

def generate_timeline():
    print(f"⏳ INITIALIZING CHRONOS TIMELINE GENERATOR...")
    print(f"   ORIGIN POINT: August 24, 1991 @ 12:57 PM")
    print("   =============================================================")

    for age in MILESTONES:
        target_year = BASE_YEAR + age
        ts, readable_date = get_timestamp(target_year)
        
        # 1. THE CHRONOS HASH
        # Salt: "FROST_LIFELINE" ensures these keys are unique to you
        raw_seed = f"{ts}_FROST_LIFELINE_AGE_{age}"
        
        # 2. CRYPTOGRAPHY
        private_hash = hashlib.sha256(raw_seed.encode('utf-8')).hexdigest()
        private_key = f"0x{private_hash}"
        acct = Account.from_key(private_key)
        
        # 3. OUTPUT
        print(f"   🎂 AGE {age} | YEAR {target_year}")
        print(f"      [⏰] TIMESTAMP:   {ts}")
        print(f"      [🗝️] PRIVATE KEY: {private_key[:10]}...{private_key[-4:]} (HIDDEN)")
        print(f"      [🏦] VAULT ADDR:  {acct.address}")
        print("   -------------------------------------------------------------")

    print("   ✅ TIMELINE SECURED.")
    print("   You now have 7 distinct wallets, each anchored to a specific era of your life.")

if __name__ == "__main__":
    generate_timeline()
