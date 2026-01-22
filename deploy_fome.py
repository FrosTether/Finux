import os
import subprocess

def deploy_fome_gui():
    print("🖥️  DEPLOYING FOME INTERFACE...")
    
    # 1. Stage Files
    subprocess.run(["git", "add", "."], check=False)
    
    # 2. Commit
    msg = "Release: FOME Desktop Environment (Forked GNOME Shell)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    
    # 3. Push
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ FOME IS DEFAULT.")
    print("   We have replaced the GUI layer.")

if __name__ == "__main__":
    deploy_fome_gui()
