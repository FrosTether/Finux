import subprocess
import sys
import os
import time

# Configuration
APK_PATH = os.path.join("bin", "FrostGlass_AR.apk")
ADB_COMMAND = "adb"

def check_adb_installed():
    """Verifies that ADB is in the system PATH."""
    try:
        subprocess.run([ADB_COMMAND, "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def get_connected_devices():
    """Returns a list of connected device IDs."""
    result = subprocess.run([ADB_COMMAND, "devices"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")[1:] # Skip first line "List of devices attached"
    devices = [line.split("\t")[0] for line in lines if "device" in line and line.strip() != ""]
    return devices

def install_apk(device_id):
    """Installs the APK to the specific device ID."""
    print(f"[❄️] Targeting device: {device_id}...")
    
    if not os.path.exists(APK_PATH):
        print(f"[!] Error: Could not find {APK_PATH}. Did you run the deployment script?")
        return

    print(f"[...] Sideloading {APK_PATH} (This may take a moment)...")
    
    # -r = Reinstall if exists, -d = Allow downgrade
    try:
        subprocess.run([ADB_COMMAND, "-s", device_id, "install", "-r", "-d", APK_PATH], check=True)
        print(f"[✅] SUCCESS: FrostGlass installed on {device_id}")
    except subprocess.CalledProcessError:
        print(f"[X] FAILURE: Could not install on {device_id}")

def main():
    print("--- Frost Protocol Sideload Automator ---")
    
    if not check_adb_installed():
        print("[!] ADB is not found. Please install Android Platform Tools.")
        sys.exit(1)

    devices = get_connected_devices()
    
    if not devices:
        print("[?] No devices found. Connect your Quest or Phone via USB and enable Debugging.")
        sys.exit(0)

    print(f"[i] Found {len(devices)} device(s).")

    for device in devices:
        install_apk(device)

if __name__ == "__main__":
    main()
