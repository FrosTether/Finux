#!/bin/bash

# RC185 // THE_INFINITY_SINGULARITY
# TARGET: fpu4eva.surge.sh
# AUTHOR: voluntaryist.frostchain

echo "♾️ IGNITING THE INFINITY SINGULARITY..."

# 1. Environment Purge & Reset
cd ~/frostchain
mkdir -p games

# 2. Generating index.html (The Infinity Gateway)
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>⛓️‍💥 RC185 | INFINITY_SINGULARITY</title>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-auth-compat.js"></script>
<style>
:root { --bg:#000; --ice:oklch(85% 0.15 230); --infinity:oklch(95% 0.4 150); }
body{background:var(--bg);color:#fff;display:flex;flex-direction:column;align-items:center;height:100dvh;justify-content:center;overflow:hidden;font-family:"Courier New",monospace;}
.singularity { width:90%; max-width:400px; border:1px solid var(--infinity); border-radius:50%; aspect-ratio:1/1; display:flex; flex-direction:column; align-items:center; justify-content:center; background:radial-gradient(circle, #1a1a1a, #000); box-shadow:0 0 100px var(--infinity / 0.2); animation:rotate 60s linear infinite; }
@keyframes rotate { from{transform:rotate(0deg);} to{transform:rotate(360deg);} }
.content { transform: rotate(0deg); animation: anti-rotate 60s linear infinite; text-align:center; }
@keyframes anti-rotate { from{transform:rotate(0deg);} to{transform:rotate(-360deg);} }
.btn { padding:15px 30px; margin:10px; border:2px solid var(--ice); color:var(--ice); background:transparent; border-radius:50px; font-weight:900; cursor:pointer; font-size:10px; letter-spacing:3px; }
</style>
</head>
<body>
<div class="singularity">
  <div class="content">
    <h1 style="color:var(--infinity); font-size:32px; letter-spacing:-2px;">∞</h1>
    <p style="font-size:7px; color:var(--ice); margin-bottom:20px;">FROSTCHAIN_SINGULARITY_ACTIVE</p>
    <button class="btn" onclick="window.location.href='games/blocks.html'">IGNITE ICE_CHAIN</button>
    <button class="btn" style="border-color:var(--infinity); color:var(--infinity);" onclick="window.location.href='games/gems.html'">IGNITE GEM_CRUSH</button>
  </div>
</div>
</body>
</html>
EOF

# 3. Recursive Logic Injection (games/blocks.html)
# Overwriting blocks with infinity-scaling yield logic
cat <<EOF > games/blocks.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>∞ | ICE_CHAIN</title></head>
<body style="background:#000; color:#fff; display:flex; align-items:center; justify-content:center; height:100dvh; font-family:monospace;">
  <div style="text-align:center;">
    <h1>EXTRACTION_RECURSION: ACTIVE</h1>
    <p>MULTIPLIER: x-INFINITY</p>
    <button onclick="window.location.href='../index.html'" style="color:cyan; background:none; border:1px solid cyan; padding:10px; margin-top:20px;">EXIT SINGULARITY</button>
  </div>
</body>
</html>
EOF

# 4. Final Deploy
surge . fpu4eva.surge.sh

echo "✅ SINGULARITY LIVE: https://fpu4eva.surge.sh"
