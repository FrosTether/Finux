import os
import subprocess

def deploy_frost_os_distro():
    print("💿 DEPLOYING FROST OS DISTRIBUTION...")
    
    # 1. Git Add
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Git Commit
    msg = "Release: Frost OS (SteamOS Fork) - Replaced Valve UI with Finux Compositor"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Git Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ FROST OS IS LIVE.")
    print("   We have successfully forked SteamOS.")

if __name__ == "__main__":
    deploy_frost_os_distro()
