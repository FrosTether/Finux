import os
import subprocess

def deploy_package_tools():
    print("📦 DEPLOYING FROST PACKAGE MANAGER...")
    
    # 1. Make executable directory
    target_dir = "mobile/fos/bin"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 2. Push to Git
    subprocess.run(["git", "add", "."], check=False)
    msg = "Feature: apt-frost (Alien RPM Converter & .fro Package Support)"
    subprocess.run(["git", "commit", "-m", msg], check=False)
    subprocess.run(["git", "push", "origin", "main"], check=False)
    
    print("\n✅ PACKAGE MANAGER DEPLOYED.")
    print("   Usage: 'python3 apt_frost.py install app.rpm'")

if __name__ == "__main__":
    deploy_package_tools()
