#!/bin/bash
# Frost OS Nightly Build & Test - Android 17 "Pumpkin Cheesecake"

# 1. Environment & Paths
export FINUX_ROOT="/finux"
export PROJECT_DIR="$HOME/frost-os-development"
export LOG_FILE="$PROJECT_DIR/logs/nightly_$(date +%Y%m%d).log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "--- [$(date)] Starting Frost OS Nightly Cycle ---"

# 2. Sync & Build Binaries
cd $PROJECT_DIR
repo sync -c -j$(nproc)

echo "[*] Building frost-crush and frostman..."
python3 scripts/frost_builder.py --release --sign

# 3. Compile System Image
source build/envsetup.sh
lunch frost_os_emulator-userdebug
make -j$(nproc)

# 4. Integrated Cold Boot Test
echo "[*] Initiating Cold Boot Validation..."
# Launching emulator in headless mode for server-side testing
emulator -avd Frost_PC_Internal -no-window -no-audio -gpu off &
EMU_PID=$!

# Wait for boot property to reach '1' (booted)
echo "[*] Waiting for kernel initialization..."
BOOT_TIMEOUT=300
TIMER=0
until [ $(adb shell getprop sys.boot_completed 2>/dev/null | grep -c "1") -eq 1 ] || [ $TIMER -ge $BOOT_TIMEOUT ]; do
    sleep 5
    ((TIMER+=5))
    echo -n "."
done

if [ $TIMER -ge $BOOT_TIMEOUT ]; then
    echo -e "\n[!] ERROR: Cold boot timed out. Build failed validation."
    kill $EMU_PID
    exit 1
else
    echo -e "\n[*] Cold boot successful. Frost OS is stable."
    kill $EMU_PID
fi

# 5. Final Deployment & GPG Backup
echo "[*] Moving verified binaries to $FINUX_ROOT..."
sudo cp build/frost-fosp $FINUX_ROOT/
./scripts/gpg_backup.sh $FINUX_ROOT/frostman

echo "--- [$(date)] Nightly Cycle Completed Successfully ---"
