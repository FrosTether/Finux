#!/data/data/com.termux/files/usr/bin/bash

# 1. Configuration
UPDATE_FILE="$HOME/Finux/updates/finux_latest.zip"
LOG_FILE="$HOME/Finux/sideload_log.txt"

echo "--- Finux Sideload Automator (2026 Build) ---"

# 2. Check for dependencies
if ! command -v adb &> /dev/null; then
    echo "ADB not found. Installing termux-adb..."
    pkg install wget -y
    curl -s https://raw.githubusercontent.com/nohajc/termux-adb/master/install.sh | bash
fi

# 3. Wait for Device Trigger (Once detected)
echo "Waiting for device in 'sideload' mode..."
while true; do
    # Check if a device is connected in sideload mode
    STATUS=$(adb devices | grep "sideload" | awk '{print $2}')
    
    if [ "$STATUS" == "sideload" ]; then
        echo "[$(date)] Device detected! Starting sideload..." | tee -a "$LOG_FILE"
        
        # 4. Execute Sideload
        if adb sideload "$UPDATE_FILE"; then
            echo "--- Update successful! ---" | tee -a "$LOG_FILE"
            # Optional: Auto-reboot after success
            # adb reboot
            exit 0
        else
            echo "Error: Sideload failed. Check the zip file." | tee -a "$LOG_FILE"
            exit 1
        fi
    fi
    
    # Wait 5 seconds before checking again to save battery
    sleep 5
done
