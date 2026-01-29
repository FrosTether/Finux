#!/bin/bash

echo "[❄️] INITIALIZING FINUX ROOT PROTOCOLS..."
echo "[i] Target: Cloud Deployment Environment"

# 1. GRANT FILE SYSTEM PERMISSIONS (The "Nuclear" Option)
# This gives every file in the current folder permission to execute.
echo "[...] Unlocking file system (chmod 777)..."
chmod -R 777 .
chmod +x *.py
echo "[✅] File system unlocked."

# 2. OPEN NETWORK PORTS (Firewall)
# Allows traffic on Port 5000 (Cloud Node) and 8080 (OTA Server)
echo "[...] Configuring Network Firewall..."
if command -v ufw >/dev/null; then
    sudo ufw allow 5000/tcp
    sudo ufw allow 8080/tcp
    echo "[✅] Ports 5000 & 8080 opened."
else
    echo "[!] UFW not found (Skipping firewall step - assume open)."
fi

# 3. CREATE SYSTEM SERVICE (Auto-Start Permission)
# This tells the Linux OS to trust your script and run it as a background service.
SERVICE_FILE="finux_node.service"

echo "[...] Generating Systemd Service File..."
cat <<EOT > $SERVICE_FILE
[Unit]
Description=Frost Protocol Cloud Node
After=network.target

[Service]
User=root
WorkingDirectory=$(pwd)
ExecStart=/usr/bin/python3 $(pwd)/FrostCloud_Node.py
Restart=always

[Install]
WantedBy=multi-user.target
EOT

echo "[✅] Service configuration created: $SERVICE_FILE"

# 4. FINAL VERIFICATION
echo "------------------------------------------------"
echo "   ❄️ PERMISSIONS GRANTED. SYSTEM READY. ❄️"
echo "------------------------------------------------"
echo "To start the Cloud Node with these new permissions, run:"
echo "   sudo python3 FrostCloud_Node.py"
echo "------------------------------------------------"
