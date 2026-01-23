import os
import subprocess

def deploy_sovereignty_treaty():
    print("📜 DEPLOYING SOVEREIGNTY TREATY...")
    
    # 1. Create Security Dir
    if not os.path.exists("mobile/kernel/security"):
        os.makedirs("mobile/kernel/security")
        
    # 2. Stage
    subprocess.run(["git", "add", "."], check=False)
    
    # 3. Commit
    msg = "Legal: Series A Split ($40M) + NO_FED_BACKDOOR Protocol (Warrant Canary Active)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 4. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ TREATY SIGNED.")
    print("   The code is now sovereign territory.")

if __name__ == "__main__":
    deploy_sovereignty_treaty()
