import os
import subprocess

def deploy_legal_framework():
    print("⚖️  DEPLOYING LEGAL & FINANCE FRAMEWORK...")
    
    # 1. Add Files
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Corporate: Series A Valuation ($120M) & USPTO Patent Filings"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ CORPORATE STRUCTURE UPDATED.")
    print("   Run 'python corporate/valuation_v2.py' to show Dusan the new price.")

if __name__ == "__main__":
    deploy_legal_framework()
