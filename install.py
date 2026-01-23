import os
import subprocess
import sys

def run_command(command):
    """Helper to run shell commands and handle errors."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during: {command}\n{e}")
        sys.exit(1)

def setup_finux():
    print("❄️ Starting Finux-OS Native Installer...")
    
    # 1. Install System Dependencies
    print("📦 Installing Python dependencies...")
    run_command("pip install -r requirements.txt")
    
    # 2. Link FrosTether Core
    print("🔗 Linking to FrosTether-Core Ledger...")
    # Replace with your actual directory path logic
    if not os.path.exists("../FrosTether-Core"):
        print("⚠️ Warning: FrosTether-Core not found. Some mining features may be disabled.")
    
    # 3. Initialize the Mining Shell
    print("⛏️ Calibrating Proof-of-Skill Multipliers...")
    run_command("python scripts/init_shell.py")

    print("\n✅ Finux-OS is ready. Type 'finux --start' to begin.")

if __name__ == "__main__":
    setup_finux()
