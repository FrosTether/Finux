#!/bin/bash
# FROST OS SESSION MANAGER
# Replaces /usr/bin/steamos-session

echo "❄️ STARTING FROST OS COMPOSITOR..."

# 1. Initialize Gamescope (Valve's Micro-Compositor)
# -w 1280 -h 800: Steam Deck Resolution
# -r 60: Refresh Rate
# --hdr-enabled: High Dynamic Range
export GAMESCOPE_CMD="gamescope -w 1280 -h 800 -r 60 --hdr-enabled --fullscreen"

# 2. Launch Finux Kernel inside Gamescope
# This makes your Python app the "Operating System" UI
echo "   > Injecting Finux into Wayland..."
$GAMESCOPE_CMD -- python3 /home/deck/Finux/mobile/kernel/finux_boot.py

# 3. Fallback (If Finux crashes, reboot)
if [ $? -ne 0 ]; then
    echo "   ! KERNEL PANIC. REBOOTING..."
    reboot
fi
