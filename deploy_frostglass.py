import os
import shutil

def deploy_frostglass():
    target_dir = "bin"
    target_apk = "FrostGlass_AR.apk"

    print(f"[❄️] Starting FrostGlass Deployment...")

    # 1. FIX: Ensure 'bin' is a directory, not a file
    if os.path.exists(target_dir):
        if not os.path.isdir(target_dir):
            print(f"[!] Alert: '{target_dir}' is a file. Removing it to create directory.")
            os.remove(target_dir)
            os.makedirs(target_dir)
    else:
        os.makedirs(target_dir)

    # 2. Logic: Find the APK and rename/move it
    # (Assuming the APK is currently in the root or downloaded location)
    current_files = [f for f in os.listdir('.') if f.endswith('.apk')]
    
    if current_files:
        latest_apk = current_files[0] # Grab the first APK found
        destination = os.path.join(target_dir, target_apk)
        
        print(f"[+] Moving {latest_apk} -> {destination}")
        shutil.move(latest_apk, destination)
        print("[✅] FrostGlass_AR successfully deployed.")
    else:
        print("[?] No .apk file found in root to deploy.")

if __name__ == "__main__":
    deploy_frostglass()
