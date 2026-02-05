#!/bin/bash

# RC191 // FROST_OS_UNIVERSAL_COMPILER
# OWNER: voluntaryist.frostchain
# TARGET: fpu4eva.surge.sh

echo "⛓️‍💥 STARTING FROST-OS COMPILATION..."

# 1. Clean Environment
mkdir -p games apps
echo "963Hz_GENESIS_LOCK" > .resonance

# 2. Compile index.html (Dashboard & Auth Gateway)
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>⛓️‍💥 FROST-OS | RC191</title>
<script src="https://cdn.jsdelivr.net/npm/ethers@6.9.0/dist/ethers.umd.min.js"></script>
<style>
:root { --bg:#000; --ice:oklch(85% 0.15 230); --leet:oklch(90% 0.4 100); --fszt:oklch(60% 0.15 250); --warn:oklch(65% 0.25 40); }
* { margin:0; padding:0; box-sizing:border-box; font-family:"Courier New", monospace; }
body { background:var(--bg); color:#fff; height:100dvh; display:flex; flex-direction:column; align-items:center; padding:20px; }
.os-header { width:100%; max-width:500px; display:flex; justify-content:space-between; align-items:center; padding-bottom:15px; border-bottom:1px solid #222; margin-bottom:30px; }
.app-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:25px; width:100%; max-width:400px; }
.app-icon { display:flex; flex-direction:column; align-items:center; cursor:pointer; }
.icon-box { width:70px; height:70px; background:#111; border:2px solid #222; border-radius:18px; display:flex; align-items:center; justify-content:center; font-size:28px; transition:0.2s; box-shadow:0 4px 15px rgba(0,0,0,0.5); }
.app-icon:active .icon-box { transform:scale(0.9); background:var(--leet); }
.app-name { font-size:8px; color:#666; margin-top:8px; text-transform:uppercase; letter-spacing:1px; }
#gate { position:fixed; inset:0; background:rgba(0,0,0,0.98); display:none; flex-direction:column; align-items:center; justify-content:center; z-index:1000; padding:30px; text-align:center; }
.gate-card { border:2px solid var(--warn); padding:25px; border-radius:20px; background:#0a0000; }
</style>
</head>
<body>
<div class="os-header">
  <div style="font-weight:900; color:var(--leet);">FROST-OS</div>
  <div style="font-size:8px; color:var(--ice); border:1px solid var(--ice); padding:2px 8px; border-radius:10px;">963Hz_SYNC</div>
</div>
<div class="app-grid">
  <div class="app-icon" onclick="openGate('blocks')"><div class="icon-box">🧱</div><div class="app-name">FrostMines</div></div>
  <div class="app-icon" onclick="openGate('gems')"><div class="icon-box">💎</div><div class="app-name">FrostCrush</div></div>
  <div class="app-icon" onclick="window.location.href='apps/fotr.html'"><div class="icon-box">📡</div><div class="app-name">FOTR</div></div>
</div>
<div id="gate"><div class="gate-card">
  <h2 style="color:var(--warn); margin-bottom:15px;">⚠️ MINING_DYNAMICS</h2>
  <p style="font-size:9px; color:#ffcccc; margin-bottom:20px; line-height:1.4;">Accept the 10% Heart Burn ❤️‍🔥 and x-Infinity power load to ignite extraction.</p>
  <button onclick="ignite()" style="width:100%; padding:15px; background:var(--leet); border:none; font-weight:900; border-radius:50px; cursor:pointer;">IGNITE</button>
</div></div>
<script>
let target = '';
function openGate(node) { target = node; document.getElementById('gate').style.display = 'flex'; }
function ignite() { window.location.href = 'games/' + target + '.html'; }
</script>
</body>
</html>
EOF

# 3. Compile games/blocks.html (FrostMines Engine)
cat <<EOF > games/blocks.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>🧱 FrostMines</title></head>
<body style="background:#000; color:cyan; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:monospace;">
  <h1>FROSTMINES_TERMINAL</h1>
  <p>SETTLEMENT: WXMR_BASE (22.5%)</p>
  <button onclick="window.location.href='../index.html'" style="margin-top:20px; color:#666; background:none; border:1px solid #333; padding:10px;">EXIT</button>
</body>
</html>
EOF

# 4. Compile games/gems.html (FrostCrush Engine)
cat <<EOF > games/gems.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>💎 FrostCrush</title></head>
<body style="background:#000; color:magenta; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:monospace;">
  <h1>FROSTCRUSH_TEMPORAL</h1>
  <p>SETTLEMENT: FsZT_MIRROR (15.0%)</p>
  <button onclick="window.location.href='../index.html'" style="margin-top:20px; color:#666; background:none; border:1px solid #333; padding:10px;">EXIT</button>
</body>
</html>
EOF

# 5. Compile apps/fotr.html (Spectrum Sync)
cat <<EOF > apps/fotr.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>📡 FOTR</title></head>
<body style="background:#000; color:lime; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; font-family:monospace;">
  <h1>FOTR_SPECTRUM_SYNC</h1>
  <p>FJTDVR...1C7s_VERIFIED</p>
  <button onclick="window.location.href='../index.html'" style="margin-top:20px; color:#666; background:none; border:1px solid #333; padding:10px;">EXIT</button>
</body>
</html>
EOF

# 6. Final Deployment
echo "🚀 DEPLOYING FROST-OS TO SPECTRUM..."
surge . fpu4eva.surge.sh

echo "✅ COMPILATION COMPLETE: https://fpu4eva.surge.sh"
