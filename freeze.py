import os
import sys
from cryptography.fernet import Fernet, InvalidToken

def load_bio_key():
    key_path = os.path.expanduser("~/.finux/frost.key")
    if not os.path.exists(key_path):
        print(">> [ERROR] Biological key missing. Run derive_frost_key.py first.")
        sys.exit(1)
    return open(key_path, "rb").read()

def frost_do(target, mode):
    key = load_bio_key()
    f = Fernet(key)
    
    # Grok 4.1 Style Reasoning Trace
    print(f">> [THINKING] Initializing Deep Freeze v2.1...")
    print(f">> Target: {target}")
    print(f">> Mode: {'FREEZE' if mode == 'freeze' else 'THAW'}")
    print(">> Key entropy: 1991-08-24 16:22:00 + Monroeville lock")
    
    if not os.path.exists(target):
        print(">> [ERROR] File not found.")
        sys.exit(1)
    
    with open(target, "rb") as file:
        data = file.read()
    
    try:
        if mode == "freeze":
            processed = f.encrypt(data)
            label = "FROZEN"
        else:
            processed = f.decrypt(data)
            label = "THAWED"
        
        with open(target, "wb") as file:
            file.write(processed)
        print(f">> TARGET {label} SUCCESSFULLY.")
        print(">> [COMPLETE] Frost Protocol secure.")
    
    except InvalidToken:
        print(">> [ERROR] Invalid key or corrupted data. Thaw failed.")
        sys.exit(1)
    except Exception as e:
        print(f">> [ERROR] {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 freeze.py <file> <freeze|thaw>")
        sys.exit(1)
    
    target_file = sys.argv[1]
    action = sys.argv[2].lower()
    if action not in ["freeze", "thaw"]:
        print(">> ACTION must be 'freeze' or 'thaw'")
        sys.exit(1)
    
    frost_do(target_file, action)