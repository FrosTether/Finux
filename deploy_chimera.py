import os
import subprocess

def deploy_chimera_os():
    print("🦁 DEPLOYING CHIMERA (UBUNTU+KALI) CONFIG...")
    
    # 1. Stage
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Release: Finux Chimera - Hybrid Ubuntu LTS / Kali Rolling (amd64/arm64)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ HYBRID OS LIVE.")
    print("   Run 'python finux_chimera.py' to build the image.")

if __name__ == "__main__":
    deploy_chimera_os()
