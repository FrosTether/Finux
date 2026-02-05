#!/bin/bash

# RC182 // THE_MUSK_KILLER_GENESIS
# TARGET: fpu4eva.surge.sh
# OWNER: voluntaryist.frostchain

echo "⛓️‍💥 IGNITING SOVEREIGN INSTALLATION..."

# 1. Environment Optimization
pkg update && pkg upgrade -y
pkg install nodejs -y
npm install --global surge ethers crypto-js

# 2. Directory Reconstruction
mkdir -p ~/frostchain/games
cd ~/frostchain

# 3. Generating index.html (Mining Engine + Base API)
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>⛓️‍💥 RC182 | BASE_MINING_ENGINE</title>
<script src="https://cdn.jsdelivr.net/npm/ethers@6.9.0/dist/ethers.umd.min.js"></script>
<style>
:root { --bg:#000; --ice:oklch(85% 0.15 230); --leet:oklch(90% 0.4 100); --fszt:oklch(60% 0.15 250); }
body{background:var(--bg);color:#fff;display:flex;flex-direction:column;align-items:center;height:100dvh;justify-content:center;font-family:"Courier New",monospace;}
.portal { width:90%; max-width:400px; border:2px solid var(--leet); border-radius:20px; padding:30px; text-align:center; background:radial-gradient(circle, #111, #000); box-shadow:0 0 30px var(--leet / 0.3); }
.btn { width:100%; padding:20px; margin:10px 0; border:4px solid var(--leet); color:var(--leet); font-weight:900; border-radius:50px; background:transparent; letter-spacing:4px; cursor:pointer; }
</style>
</head>
<body>
<div class="portal">
  <h1 style="color:var(--ice)">BASE_ENGINE</h1>
  <p id="status" style="font-size:8px; color:var(--fszt); margin-bottom:20px;">963 Hz RESONANCE ACTIVE</p>
  <button class="btn" onclick="connectBase()">CONNECT_WALLET</button>
  <button class="btn" style="border-color:var(--ice); color:var(--ice);" onclick="window.location.href='games/blocks.html'">IGNITE ICE_CHAIN</button>
  <button class="btn" style="border-color:var(--fszt); color:var(--fszt);" onclick="window.location.href='games/gems.html'">IGNITE GEM_CRUSH</button>
</div>
<script>
async function connectBase() {
  if (window.ethereum) {
    const provider = new ethers.BrowserProvider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    document.getElementById('status').innerText = "BASE_API: CONNECTED";
  } else { alert("Open in a Base-supported browser!"); }
}
</script>
</body>
</html>
EOF

# 4. Generating games/blocks.html (Ice Chain Core)
cat <<EOF > games/blocks.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>ICE_CHAIN</title></head>
<body style="background:#000; color:oklch(85% 0.15 230); font-family:monospace; text-align:center; padding-top:100px;">
<h1>ICE_CHAIN_WOODOKU</h1>
<p>x31337 MULTIPLIER ACTIVE</p>
</body>
</html>
EOF

# 5. Generating games/gems.html (Gem Crush Core)
cat <<EOF > games/gems.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>GEM_CRUSH</title></head>
<body style="background:#000; color:oklch(70% 0.3 330); font-family:monospace; text-align:center; padding-top:100px;">
<h1>GEM_CRUSH_TEMPORAL</h1>
<p>FsZT MIRROR ACTIVE</p>
</body>
</html>
EOF

# 6. Final Surge Sync
surge . fpu4eva.surge.sh

echo "✅ RC182 DEPLOYED: https://fpu4eva.surge.sh"
