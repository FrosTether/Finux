import os
import subprocess

def deploy_deal_pressure():
    print("🔥 DEPLOYING DEAL PRESSURE PROTOCOLS...")
    
    # 1. Add
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Corporate: Investor Waitlist Active (Google M&A queued as backup)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ WAR ROOM ACTIVE.")
    print("   Run 'python corporate/finance/deal_war_room.py' to show him the queue.")

if __name__ == "__main__":
    deploy_deal_pressure()
