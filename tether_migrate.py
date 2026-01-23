from beem import Steem
from beem.account import Account
import json

# Connect to Main Steem.it to pull data
main_steem = Steem(node="https://api.steemit.com")
account_name = "agorajat"

def generate_tether_snapshot(name):
    acc = Account(name, steem_instance=main_steem)
    
    # Capture Holdings
    snapshot = {
        "account": acc.name,
        "steem_balance": str(acc['balance']),
        "sbd_balance": str(acc['sbd_balance']),
        "vesting_shares": str(acc['vesting_shares']),
        "reputation": acc['reputation'],
        "doge_principle": "Do Only Good Everyday"
    }
    
    # Save for amiah.do Genesis injection
    with open('amiah_genesis_entry.json', 'w') as f:
        json.dump(snapshot, f, indent=4)
    print(f"✅ Snapshot for @{name} captured. Ready for amiah.do fork.")

generate_tether_snapshot(account_name)
