import os
import subprocess

def deploy_deal_docs():
    print("💼 DEPLOYING TERM SHEET PROTOCOLS...")
    
    target = "corporate/offer_elon.py"
    
    # 1. Stage
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Corporate: Series A Term Sheet - Strategic Investor (X Corp)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ OFFER LIVE ON CHAIN.")
    print("   Run 'python corporate/offer_elon.py' to trigger the transmission.")

if __name__ == "__main__":
    deploy_deal_docs()
