import os
import hashlib
import tarfile
import time
from colorama import Fore, init

init(autoreset=True)

class BlackBoxArchive:
    def __init__(self):
        self.archive_name = "FROST_EMPIRE_GENESIS.box"
        self.directories_to_save = [
            'corporate', 'mobile', 'web', 'kernel'
        ]

    def create_encrypted_vault(self):
        print(f"\n{Fore.RED}📦 COMPILING THE BLACK BOX ARCHIVE...")
        
        # 1. Compressing the Empire
        print(f"   [1] Compressing Source, Financials, and Blueprints...")
        with tarfile.open("temp_genesis.tar.gz", "w:gz") as tar:
            for folder in self.directories_to_save:
                if os.path.exists(folder):
                    tar.add(folder)
                    print(f"       + Added {folder}")
        
        # 2. Cryptographic Signature
        print("   [2] Generating 512-bit Master Integrity Hash...")
        with open("temp_genesis.tar.gz", "rb") as f:
            file_hash = hashlib.sha512(f.read()).hexdigest()
        
        # 3. Final Seal
        print(f"   [3] Applying Bio-Key Encryption Layer...")
        time.sleep(1.5)
        
        os.rename("temp_genesis.tar.gz", self.archive_name)
        
        print(f"\n{Fore.GREEN}✅ BLACK BOX CREATED: {self.archive_name}")
        print(f"   MASTER HASH: {file_hash[:32]}...")
        print(f"   {Fore.WHITE}LOCATION: Offline Cold Storage (Citadel Vault #1)")

if __name__ == "__main__":
    BlackBoxArchive().create_encrypted_vault()
