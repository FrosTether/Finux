#!/bin/bash

# RC188 // BASE_API_QUANTUM_INJECTOR
# TARGET: fpu4eva.surge.sh
# AUTHOR: voluntaryist.frostchain

echo "⛓️‍💥 INJECTING BASE_API INTO EXTRACTION NODES..."

# 1. Directory Lock
cd ~/frostchain

# 2. Re-Building index.html (Master Portal with Multi-Auth + Base API)
cat <<EOF > index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<title>⛓️‍💥 RC188 | BASE_PORTAL</title>
<script src="https://cdn.jsdelivr.net/npm/ethers@6.9.0/dist/ethers.umd.min.js"></script>
<style>
:root { --bg:#000; --ice:oklch(85% 0.15 230); --leet:oklch(90% 0.4 100); --base:#0052ff; }
body {
  background: var(--bg); color: #fff; height: 100dvh; display: flex; flex-direction: column; 
  align-items: center; justify-content: center; font-family: "Courier New", monospace;
  background: radial-gradient(circle at center, rgba(0,82,255,0.1) 0%, #000 70%);
}
.portal { width:90%; max-width:400px; border:2px solid var(--base); border-radius:20px; padding:30px; text-align:center; background:#050505; box-shadow:0 0 40px var(--base / 0.3); }
.btn { width:100%; padding:18px; margin:10px 0; border:4px solid var(--base); color:var(--base); font-weight:900; border-radius:50px; background:transparent; letter-spacing:4px; cursor:pointer; font-size:12px; }
</style>
</head>
<body>
<div class="portal">
  <h1 style="color:var(--ice); font-size:28px;">BASE_ENGINE</h1>
  <p id="status" style="font-size:8px; color:var(--ice); margin-bottom:20px;">FJTDVR...1C7s_SIGNED</p>
  <button class="btn" onclick="connectBase()">CONNECT_WALLET</button>
  <button class="btn" style="border-color:var(--leet); color:var(--leet);" onclick="window.location.href='games/blocks.html'">IGNITE ICE_CHAIN</button>
  <button class="btn" style="border-color:var(--ice); color:var(--ice);" onclick="window.location.href='games/gems.html'">IGNITE GEM_CRUSH</button>
</div>
<script>
async function connectBase() {
  if (window.ethereum) {
    const provider = new ethers.BrowserProvider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    document.getElementById('status').innerText = "BASE_API: CONNECTED_8453";
  } else { alert("Install a Base Wallet!"); }
}
</script>
</body>
</html>
EOF

# 3. Injecting Base API Bridge into games/blocks.html
cat <<EOF > games/blocks.html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>ICE_CHAIN_BASE</title>
<script src="https://cdn.jsdelivr.net/npm/ethers@6.9.0/dist/ethers.umd.min.js"></script>
</head>
<body style="background:#000; color:#fff; display:flex; align-items:center; justify-content:center; height:100dvh; font-family:monospace;">
  <div style="text-align:center;">
    <h1>ICE_CHAIN_CORE: ACTIVE</h1>
    <p>BASE_API_SETTLEMENT: ENABLED</p>
    <p style="color:cyan;">x-INFINITY_OVERDRIVE</p>
  </div>
</body>
</html>
EOF

# 4. Final Deployment Sync
surge . fpu4eva.surge.sh

echo "✅ BASE_API INJECTED: https://fpu4eva.surge.sh"
