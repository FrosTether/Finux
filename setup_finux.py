./bootloader.sh
import sys
import subprocess
import os
import platform

# --- CONFIGURATION ---
REQUIRED_PACKAGES = [
    "PyQt6",           # The GUI Framework
    "psutil",          # System Monitoring (CPU/RAM)
    "web3",            # Blockchain Interaction
    "py-solc-x",       # Solidity Compiler
    "qdarktheme",      # Dark Mode Theme
    "requests"         # General Networking
]

REQUIRED_FILES = [
    "FUI.py",
    "governance_tool.py",
    "bootloader.sh",
    "FrostGovernance.sol"
]

def print_step(msg):
    print(f"\n🔹 {msg}")

def print_success(msg):
    print(f"✅ {msg}")

def print_error(msg):
    print(f"❌ {msg}")

def install_package(package):
    """Installs a Python package via pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print_success(f"Installed {package}")
    except subprocess.CalledProcessError:
        print_error(f"Failed to install {package}")

def check_files():
    """Checks if core Finux files exist."""
    print_step("Checking Core Files...")
    missing = []
    for f in REQUIRED_FILES:
        if os.path.exists(f):
            print_success(f"Found {f}")
        else:
            print_error(f"Missing {f}")
            missing.append(f)
    
    if missing:
        print("\n⚠️  WARNING: Some files are missing. Ensure you have cloned the full repo.")
    else:
        print_success("All core files present.")

def make_bootloader_executable():
    """Ensures the bootloader script has run permissions (Linux/Mac)."""
    if platform.system() != "Windows":
        print_step("Configuring Bootloader Permissions...")
        boot_script = "bootloader.sh"
        if os.path.exists(boot_script):
            try:
                os.chmod(boot_script, 0o755)
                print_success(f"Made {boot_script} executable.")
            except Exception as e:
                print_error(f"Could not change permissions: {e}")
        else:
            print_error(f"{boot_script} not found.")

def main():
    print("========================================")
    print("❄️  FINUX ENVIRONMENT SETUP WIZARD")
    print("========================================")
    
    # 1. System Check
    print_step(f"Detected System: {platform.system()} {platform.release()}")
    
    # 2. Install Dependencies
    print_step("Installing Dependencies...")
    for package in REQUIRED_PACKAGES:
        print(f"   ... checking {package}")
        try:
            __import__(package.replace("-", "_").split("==")[0])
            print_success(f"{package} is already installed.")
        except ImportError:
            install_package(package)

    # 3. Solc (Solidity Compiler) Setup
    print_step("Initializing Solidity Compiler...")
    try:
        from solcx import install_solc
        install_solc("0.8.0")
        print_success("Solc v0.8.0 ready.")
    except Exception as e:
        print_error(f"Solc setup failed: {e}")

    # 4. File Integrity Check
    check_files()

    # 5. Linux Specific Setup
    make_bootloader_executable()

    print("\n========================================")
    print("❄️  SETUP COMPLETE")
    print("========================================")
    print("To start the Finux OS, run:")
    print("   ./bootloader.sh")
    print("========================================")

if __name__ == "__main__":
    main()
./bootloader.sh
