import os
import subprocess

def deploy_google_strategy():
    print("🤖 DEPLOYING GOOGLE STRATEGY...")
    
    # 1. Create Directory
    if not os.path.exists("corporate/partnerships"):
        os.makedirs("corporate/partnerships")
    
    # 2. Git Sequence
    subprocess.run(["git", "add", "."], check=False)
    
    # 3. Commit
    msg = "Corporate: Strategic Inquiry - Alphabet Inc. (Counter-balancing X Holdings)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 4. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ STRATEGY LIVE.")
    print("   Run 'python corporate/partnerships/ask_google.py' to see their counter-offer.")

if __name__ == "__main__":
    deploy_google_strategy()
