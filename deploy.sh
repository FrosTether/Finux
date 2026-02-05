#!/bin/bash

# 1. PREPARE ENVIRONMENT
echo ">> INITIALIZING FINUX 2.4.1 STABLE DEPLOYMENT..."
mkdir -p www/games www/system www/assets/audio

# 2. SYNC CORE FILES (Preserving Ver 2.4.1 Logic)
# Integrating your stable dashboard from current snapshot
cat << 'EOF' > www/index.html
<!DOCTYPE html><html><head><title>FrostOS | Main Dashboard</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<style>
    body { background: radial-gradient(circle, #2d241f 0%, #1a120e 100%); color: white; font-family: sans-serif; margin: 0; overflow: hidden; }
    .widget { background: rgba(45, 30, 25, 0.9); border: 2px solid #8d6e63; border-radius: 15px; padding: 15px; margin: 10px; }
    .wallet-widget { border-color: #ffb74d; }
    .fota-badge { background: rgba(102, 187, 106, 0.2); color: #66bb6a; padding: 5px; border-radius: 20px; font-size: 0.7rem; }
</style>
</head>
<body>
    <div class="widget wallet-widget">
        <div>GRAYSON'S WALLET</div>
        <div style="font-size: 2rem; color: #ffb74d;" id="bal">0.000 FTC</div>
    </div>
    <div class="widget">
        <div class="fota-badge">Ver 2.4.1 (Stable)</div>
        <p>FAI 🪵🪓: ONLINE</p>
    </div>
    <div style="display:flex; justify-content:space-around;">
        <button onclick="location.href='games/icechain.html'">MINE ICECHAIN</button>
    </div>
    <script>document.getElementById('bal').innerText = (localStorage.getItem('ftc_bal') || "0.000") + " FTC";</script>
</body></html>
EOF

# 3. GITHUB SYNC (FrosTether Repo)
echo ">> SYNCING TO GITHUB REPOSITORY..."
git add .
git commit -m "Deploy: Finux Ver 2.4.1 Stable [FAI + Grayson Sync]"
git push origin main

# 4. SURGE DEPLOYMENT
echo ">> DEPLOYING TO finux241.surge.sh..."
surge www finux241.surge.sh

echo ">> ✅ DEPLOYMENT COMPLETE & REPO UPDATED."
