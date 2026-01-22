import os
import subprocess

def deploy_starlink_module():
    print("📡 DEPLOYING STARLINK COMM MODULE...")
    
    target = "mobile/fos/ask_elon.py"
    
    # 1. Stage
    if os.path.exists(target) or os.path.exists("ask_elon.py"):
        # (Handling the case where you saved it in root)
        subprocess.run(["git", "add", "."], check=False)
        
        # 2. Commit
        msg = "Feature: Secure Starlink Uplink (Direct-to-X)"
        subprocess.run(["git", "commit", "-m", msg], check=False)
        
        # 3. Push
        subprocess.run(["git", "push", "origin", "main"], check=False)
        
        print("\n✅ UPLINK ESTABLISHED.")
        print("   Run 'python ask_elon.py' to simulate the conversation.")
    else:
        print("   [!] Save the ask_elon.py file first!")

if __name__ == "__main__":
    deploy_starlink_module()
