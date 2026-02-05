#!/bin/bash

# 1. Create Folder Structure
echo ">> INITIALIZING FROSTOS DEPLOYMENT..."
mkdir -p FrostOS/games FrostOS/system
cd FrostOS

# 2. Create System API (FIP + Wallet)
cat << 'EOF' > system/api.js
const FrostOS = {
    FIP: {
        compress: (grid) => {
            let binary = grid.join('');
            let hex = "";
            for (let i = 0; i < binary.length; i += 4) {
                hex += parseInt(binary.substr(i, 4).padEnd(4, '0'), 2).toString(16);
            }
            return hex;
        }
    },
    Wallet: {
        update: (amount) => {
            let bal = parseFloat(localStorage.getItem('ftc_bal') || 0);
            localStorage.setItem('ftc_bal', (bal + amount).toFixed(4));
            window.dispatchEvent(new Event('balanceUpdate'));
        },
        get: () => localStorage.getItem('ftc_bal') || "0.0000"
    }
};
EOF

# 3. Create Launcher (index.html)
cat << 'EOF' > index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>FrostOS | Home</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        :root { --bg: #050a1f; --text: #e0f7fa; --neon-cyan: #00f3ff; }
        body { margin: 0; background: radial-gradient(circle at center, #1a2a50 0%, var(--bg) 100%); color: var(--text); font-family: 'Courier New', monospace; height: 100vh; overflow: hidden; }
        .app-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 30px; }
        .app-icon { display: flex; flex-direction: column; align-items: center; text-decoration: none; color: inherit; }
        .icon-box { width: 60px; height: 60px; border-radius: 15px; border: 1px solid var(--neon-cyan); display: flex; justify-content: center; align-items: center; font-size: 1.8rem; margin-bottom: 8px; box-shadow: 0 0 10px var(--neon-cyan); }
    </style>
</head>
<body>
    <div style="padding: 10px; background: rgba(0,0,0,0.5); font-size: 0.8rem;">FROST.OS SYSTEM ACTIVE</div>
    <div class="app-grid">
        <a href="system/vault.html" class="app-icon"><div class="icon-box">🔐</div><div>WALLET</div></a>
        <a href="games/blocks.html" class="app-icon"><div class="icon-box" style="border-color:#bc13fe">🧩</div><div>BLOCKS</div></a>
        <a href="system/myfrost.html" class="app-icon"><div class="icon-box">❄️</div><div>PROFILE</div></a>
    </div>
</body>
</html>
EOF

# 4. Create IceChain with Firestart & 852Hz (games/blocks.html)
cat << 'EOF' > games/blocks.html
<!DOCTYPE html>
<html>
<head>
    <title>IceChain | 852Hz</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <style>
        body { background: #000; color: #00f3ff; font-family: 'Courier New', monospace; margin: 0; overflow: hidden; }
        #firestart { position: fixed; inset: 0; background: #000; z-index: 99; display: flex; flex-direction: column; justify-content: center; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(9, 1fr); gap: 2px; width: 90vw; margin: 20px auto; border: 2px solid #bc13fe; }
        .cell { aspect-ratio: 1; background: rgba(188, 19, 254, 0.1); }
    </style>
</head>
<body>
    <div id="firestart"><div>> FIRESTART.EXE BOOTING...</div><div id="log"></div></div>
    <div style="padding: 10px; display: flex; justify-content: space-between;">
        <span>ICECHAIN NODE</span>
        <span id="ftc-display">0.0000 FTC</span>
    </div>
    <div class="grid" id="grid"></div>

    <script src="../system/api.js"></script>
    <script>
        const steps = ["FIP Engine: OK", "852Hz Resonance: LOADED", "Grayson Ledger: SYNCED"];
        let s = 0;
        const i = setInterval(() => {
            document.getElementById('log').innerHTML += `<div>[OK] ${steps[s]}</div>`;
            s++;
            if(s >= steps.length) {
                clearInterval(i);
                setTimeout(() => document.getElementById('firestart').style.display='none', 500);
            }
        }, 400);

        for(let j=0; j<81; j++) {
            const c = document.createElement('div');
            c.className = 'cell';
            document.getElementById('grid').appendChild(c);
        }
    </script>
</body>
</html>
EOF

# 5. Create Grayson's Vault (system/vault.html)
cat << 'EOF' > system/vault.html
<!DOCTYPE html>
<html>
<head>
    <style>body{background:#000;color:#ffd700;font-family:monospace;padding:20px;}.card{border:2px solid #ffd700;padding:20px;text-align:center;}</style>
</head>
<body>
    <div class="card">
        <h2>GRAYSON'S VAULT</h2>
        <h1 id="bal">0.0000</h1>
        <p>FROSTCOIN (FTC)</p>
    </div>
    <script>document.getElementById('bal').innerText = localStorage.getItem('ftc_bal') || "0.0000";</script>
</body>
</html>
EOF

# 6. Create Profile (system/myfrost.html)
cat << 'EOF' > system/myfrost.html
<!DOCTYPE html>
<html>
<head><style>body{background:#050a1f;color:#00f3ff;font-family:monospace;padding:20px;}</style></head>
<body>
    <h2>USER: JACOB FROST</h2>
    <p>DEV_ID: FrosTether</p>
    <p>NODE: Sylvania, OH</p>
    <button onclick="location.href='../index.html'">BACK</button>
</body>
</html>
EOF

chmod +x games/blocks.html
echo ">> DEPLOYMENT COMPLETE. OPEN index.html TO START."
