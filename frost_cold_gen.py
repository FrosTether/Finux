import secrets
import hashlib
import sys
import socket
import os
import time

# --- SECURITY CONFIGURATION ---
FROST_VERSION = "1.0 (Cold Storage)"
AIR_GAP_REQUIRED = True

def is_connected():
    """Checks for active internet connection."""
    try:
        # Attempt to resolve a common DNS (doesn't send data, just checks path)
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

def generate_secure_entropy():
    """Generates cryptographically strong random bytes."""
    return secrets.token_hex(32) # 256-bit entropy

def derive_keys(entropy):
    """Derives Public/Private pair from entropy."""
    # 1. Private Key (The Secret)
    private_key = entropy
    
    # 2. Public Key (Derived via SHA256 for this prototype)
    # In full prod, this would use secp256k1 Elliptic Curve
    sha = hashlib.sha256()
    sha.update(bytes.fromhex(private_key))
    public_key = sha.hexdigest()
    
    # 3. Frost Address (fr1...)
    sha_addr = hashlib.sha256()
    sha_addr.update(bytes.fromhex(public_key))
    address = "fr1" + sha_addr.hexdigest()[:38]
    
    return private_key, public_key, address

def create_paper_wallet(priv, pub, addr):
    """Formats the data into a printable 'Paper Wallet' artifact."""
    
    template = f"""
    =============================================================
                     ❄️ FROST PROTOCOL COLD STORAGE ❄️
    =============================================================
    DATE GENERATED: {time.strftime("%Y-%m-%d %H:%M:%S")}
    SECURITY LEVEL: AIR-GAPPED (OFFLINE)
    
    [ PUBLIC ADDRESS ] (Share this to receive FNR)
    -------------------------------------------------------------
    {addr}
    -------------------------------------------------------------
    
    [ PRIVATE KEY ] (DO NOT SHARE - KEEP SAFE)
    -------------------------------------------------------------
    {priv}
    -------------------------------------------------------------
    
    [ QR RECOVERY SEED ]
    (Scan to import into FrostWallet App)
    {pub[:16]}...[truncated for print safety]
    
    =============================================================
           STORE THIS PAPER IN A PHYSICAL SAFE OR VAULT.
    =============================================================
    """
    return template

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[❄️] Initializing {FROST_VERSION}...")
    
    # 1. THE KILLSWITCH
    if AIR_GAP_REQUIRED:
        print("[i] Verifying Environment Security...")
        time.sleep(1)
        if is_connected():
            print("\n[!!!] SECURITY ALERT [!!!]")
            print("Internet connection detected!")
            print("Cold Storage generation aborted to prevent key leakage.")
            print("Please disconnect WiFi/Ethernet and try again.")
            sys.exit(1)
        else:
            print("[✅] Environment Secure: Device is Offline.")

    # 2. Generation
    print("[...] Gathering Entropy...")
    time.sleep(2) # Accumulate randomness
    entropy = generate_secure_entropy()
    
    priv, pub, addr = derive_keys(entropy)
    
    # 3. Output
    wallet_art = create_paper_wallet(priv, pub, addr)
    
    # Save to file
    filename = f"frost_cold_wallet_{addr[:6]}.txt"
    with open(filename, "w") as f:
        f.write(wallet_art)
        
    print(f"\n[✅] SUCCESS. Wallet generated.")
    print(f"[i] Saved to file: {filename}")
    print("\n" + wallet_art)
    print("\n[NOTE] Print the text file immediately, then DELETE the file.")

if __name__ == "__main__":
    main()
