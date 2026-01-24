#!/bin/bash
# Finux OS (FOSP) - Game Installer
# Target: Yu-Gi-Oh: Frost Genesis v1.0

echo "Checking Frost Protocol permissions..."
if [[ $FOSP_USER != "Jacob" ]]; then
    echo "Access Denied: Genesis Key required."
    exit 1
fi

# 1. Create Game Partition
mkdir -p /mnt/frost/games/yugi_genesis

# 2. Link Frost Protocol Ledger for Card Verification
fosp-cli link --ledger frost_protocol_v2 --asset FNR

# 3. Pull Assets (Oofmon sprites + 311Hz Audio pack)
fosp-pkg install raylib-fosp libfrost-audio

# 4. Compile Game Logic
g++ -o /usr/bin/frost-yugi main_engine.cpp -lraylib -lfrost-protocol

echo "Deployment Successful. Run 'frost-yugi --duel' to start."
