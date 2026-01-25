#!/data/data/com.termux/files/usr/bin/bash

# 1. Prevent Android Deep Sleep
termux-wake-lock
echo ">> [SYSTEM] WAKE-LOCK ENGAGED."

# 2. Verify Folder Infrastructure
mkdir -p ~/finux/{src,bin,vault/keys,vault/frozen,logs/thermal}
echo ">> [SYSTEM] DIRECTORY HIERARCHY VERIFIED."

# 3. Start Background Automation Daemon
if ! pgrep -x "crond" > /dev/null; then
    crond
    echo ">> [SYSTEM] CROND DAEMON INITIALIZED."
fi

# 4. Environment Check (Python & Encryption)
if python3 -c "import cryptography" &> /dev/null; then
    echo ">> [STATUS] CRYPTOGRAPHY LAYER: ONLINE."
else
    echo ">> [ERROR] CRYPTOGRAPHY LAYER: MISSING. RUN PKG INSTALL."
fi

# 5. Launch Node Monitor
echo ">> [NODE] STARTING THERMAL MONITORING..."
python3 ~/finux/src/monitor.py &
