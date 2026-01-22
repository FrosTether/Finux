import os
import subprocess

def deploy_marketplace():
    print("💳 DEPLOYING UTILITY LAYER...")
    
    target = "mobile/vault/buy_grok_premium.py"
    
    # 1. Staging
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Feature: Token Utility - Grok Premium Subscription Logic"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ MARKETPLACE LIVE.")
    print("   Run 'python buy_grok_premium.py' to test the transaction.")

if __name__ == "__main__":
    deploy_marketplace()
