#!/bin/bash
# NETWORK FAILOVER: GROUND -> SPACE

LOCAL_IP="192.168.1.1"
SAT_DRIVER="python3 /home/deck/Finux/mobile/kernel/drivers/starlink_uplink.py"

echo "🔍 MONITORING GROUND CONNECTION..."

while true; do
    ping -c 1 8.8.8.8 > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "🚨 GROUND LINK SEVERED. INITIATING STARLINK FAILOVER..."
        $SAT_DRIVER
        # Re-route all traffic through Starlink interface
        ip route add default dev starlink0
        break
    fi
    sleep 5
done
