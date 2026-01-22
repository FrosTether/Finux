import os
import subprocess

def deploy_corporate_docs():
    print("👔 DEPLOYING VALUATION DOCUMENTS...")
    
    # Create directory if it doesn't exist
    if not os.path.exists("corporate"):
        os.makedirs("corporate")
        
    # Move the file (Simulation logic)
    # Ensure you saved company_valuation.py first!
    if os.path.exists("company_valuation.py"):
        os.rename("company_valuation.py", "corporate/company_valuation.py")
    
    # Git Sequence
    subprocess.run(["git", "add", "."], check=False)
    subprocess.run(["git", "commit", "-m", "Corporate: Series A Valuation Model ($50M Cap)"], check=False)
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ VALUATION LIVE.")
    print("   Run 'python corporate/company_valuation.py' to present the numbers.")

if __name__ == "__main__":
    deploy_corporate_docs()
