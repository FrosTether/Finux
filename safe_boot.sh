#!/bin/bash

FAIL_COUNT_FILE="/tmp/fui_fail_count"
MAX_RETRIES=3

# 1. Check for manual override
echo "Booting Finux OS..."
echo "Press 's' within 3 seconds for Safe Mode (CLI)..."
read -t 3 -n 1 key

if [[ $key = "s" ]]; then
    echo ">> Manual Safe Mode Triggered."
    exec /bin/bash
fi

# 2. Check Crash Loop Counter
if [ -f "$FAIL_COUNT_FILE" ]; then
    count=$(cat "$FAIL_COUNT_FILE")
    if [ "$count" -ge "$MAX_RETRIES" ]; then
        echo ">> CRITICAL: FUI crashed $count times. Dropping to Safe Mode."
        rm "$FAIL_COUNT_FILE" # Reset counter after safe mode entry
        exec /bin/bash
    fi
fi

# 3. Attempt to launch FOME FUI
echo ">> Launching FUI..."
# Increment fail counter before launch
current_count=$(cat "$FAIL_COUNT_FILE" 2>/dev/null || echo 0)
echo $((current_count + 1)) > "$FAIL_COUNT_FILE"

# Launch Interface
if python3 /home/frost/finux/fui/FUI.py; then
    # If FUI closes cleanly (exit code 0), remove fail counter
    rm "$FAIL_COUNT_FILE"
else
    # If FUI crashes, the script loops or system reboots, keeping the counter high
    echo ">> FUI Crashed!"
fi
