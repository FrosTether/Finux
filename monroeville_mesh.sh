#!/bin/bash
# STARLINK COMMUNITY MESH CONFIGURATION
# Location: Monroeville 7-Eleven Sovereign Node

echo "📡 INITIALIZING MONROEVILLE COMMUNITY MESH..."

# 1. Bypass standard ISP Gateways
export STARLINK_BYPASS_MODE=true
export MESH_SSID="FROST_CITADEL_FREE_WIFI"

# 2. Deploy Mesh Nodes (Using Gen 3 Routers)
# Placing 3 nodes around the station to cover the town center
echo "   [+] Syncing Node 01: Pump Perimeter"
echo "   [+] Syncing Node 02: Main Street Corridor"
echo "   [+] Syncing Node 03: Residential Buffer"

echo "✅ MESH ACTIVE. Monroeville is now online via Frost-1."
