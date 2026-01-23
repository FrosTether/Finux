from bitcoinlib.keys import Key
from bitcoinlib.wallets import Wallet, wallet_delete_if_exists

def inject_key(private_key_wif, wallet_name="FrostLegacy"):
    """Imports a recovered Blockchain.info key into a new project."""
    try:
        # 1. Create a Key object from the WIF string
        k = Key(private_key_wif)
        
        # 2. Initialize a new wallet for your project
        wallet_delete_if_exists(wallet_name)
        w = Wallet.create(wallet_name, keys=k, network='bitcoin')
        
        print(f"✅ Success! Key injected.")
        print(f"Legacy Address: {w.get_key().address}")
        print(f"Current Balance: {w.balance_update()} BTC")
        
    except Exception as e:
        print(f"❌ Injection Failed: {e}")

# Replace with your recovered WIF key
# inject_key("5YourRecoveredPrivateKeyGoesHere")
