#!/bin/bash

# RC180 // GENESIS_INSTALLER
# TARGET: fpu4eva.surge.sh
# OWNER: Jacob Frost (voluntaryist.frostchain)

echo "⛓️‍💥 INITIALIZING SOVEREIGN DEPLOYMENT..."

# 1. Environment Sync
pkg update && pkg upgrade -y
pkg install nodejs -y
npm install --global surge

# 2. Directory Reconstruction (Fixing 404 Routing)
mkdir -p ~/frostchain/games
cd ~/frostchain

# 3. Generating index.html (Mining Engine Portal)
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>⛓️‍💥 RC180 | MINING_ENGINE</title>
<style>
:root { --bg:#000; --ice:oklch(85% 0.15 230); --leet:oklch(90% 0.4 100); --fszt:oklch(60% 0.15 250); }
body{background:var(--bg);color:#fff;display:flex;flex-direction:column;align-items:center;height:100dvh;justify-content:center;font-family:"Courier New",monospace;}
.portal { width:90%; max-width:400px; border:2px solid var(--leet); border-radius:20px; padding:30px; text-align:center; background:radial-gradient(circle, #111, #000); }
.btn { width:100%; padding:20px; margin:10px 0; border:4px solid var(--leet); color:var(--leet); font-weight:900; border-radius:50px; background:transparent; letter-spacing:4px; cursor:pointer; }
</style>
</head>
<body>
<div class="portal">
  <h1 style="color:var(--ice)">FROST_MINES</h1>
  <p style="font-size:8px; color:var(--fszt); margin-bottom:20px;">FsZT (USDC_🪞) MIRROR_SYNC ACTIVE</p>
  <button class="btn" onclick="window.location.href='games/blocks.html'">IGNITE ICE_CHAIN</button>
  <button class="btn" style="border-color:var(--fszt); color:var(--fszt);" onclick="window.location.href='games/gems.html'">IGNITE GEM_CRUSH</button>
</div>
</body>
</html>
EOF

# 4. Generating games/blocks.html (Ice Chain Woodoku)
cat <<EOF > games/blocks.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><title>ICE_CHAIN</title>
<style>body{background:#000;color:oklch(85% 0.15 230);display:flex;align-items:center;justify-content:center;height:100dvh;}</style>
</head>
<body><h1>ICE_CHAIN_CORE: 963Hz_LOCKED</h1></body>
</html>
EOF

# 5. Generating games/gems.html (Gem Crush Engine)
cat <<EOF > games/gems.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><title>GEM_CRUSH</title>
<style>body{background:#000;color:oklch(70% 0.3 330);display:flex;align-items:center;justify-content:center;height:100dvh;}</style>
</head>
<body><h1>GEM_CORE: x31337_OVERDRIVE</h1></body>
</html>
EOF

# 6. Satoshi Zero Genesis Lock
echo "963Hz_GENESIS_LOCK_CERTIFIED" > .resonance
echo "alias sign='echo \"FJTDVR...1C7s SIGNED\"'" >> ~/.bashrc

# 7. Final Surge Push
echo "🚀 DEPLOYING TO GLOBAL SPECTRUM..."
surge . fpu4eva.surge.sh

echo "✅ GENESIS COMPLETE: https://fpu4eva.surge.sh"
