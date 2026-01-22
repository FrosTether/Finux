import os
import subprocess

def deploy_genesis_protocol():
    print("🧬 DEPLOYING GENESIS PULSE PROTOCOL...")
    
    target = "GRAYSONS_WALLET_BUILD/birth_genesis.py"
    
    # 1. Check File
    if os.path.exists(target):
        # 2. Git Sequence
        cmds = [
            ["git", "add", target],
            ["git", "commit", "-m", "Core: Wallet Linked to Biological Birth Second (1991)"],
            ["git", "push", "origin", "main"]
        ]
        
        for cmd in cmds:
            try:
                subprocess.run(cmd, check=False)
                print(f"   [OK] {' '.join(cmd)}")
            except:
                pass
            
        print("\n✅ GENESIS MAKER LIVE.")
        print("   Run 'python birth_genesis.py' to generate the key.")
    else:
        print(f"   [!] Error: File {target} not found. Save it first!")

if __name__ == "__main__":
    deploy_genesis_protocol()
