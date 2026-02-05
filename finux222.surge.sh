#!/bin/bash
# FINUX 2.2.2 CORE REBUILDER

echo ">> BUILDING FINUX 2.2.2..."
mkdir -p www/games www/system www/assets

# Create System API
cat << 'EOF' > www/system/api.js
const Finux = {
    FIP: {
        compress: (g) => g.map(v => v ? '1' : '0').join('').match(/.{1,4}/g).map(b => parseInt(b.padEnd(4,'0'), 2).toString(16)).join(''),
    },
    FAI: {
        status: "STABLE 2.2.2",
        mode: "WOOD_CHOPPER 🪵🪓"
    },
    Wallet: {
        update: (a) => {
            let b = parseFloat(localStorage.getItem('ftc_bal') || 0);
            localStorage.setItem('ftc_bal', (b + a).toFixed(4));
            window.dispatchEvent(new Event('balanceUpdate'));
        },
        get: () => localStorage.getItem('ftc_bal') || "0.0000"
    }
};
EOF

# Create Main Dashboard
cat << 'EOF' > www/index.html
<!DOCTYPE html><html><head><title>FINUX 2.22</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
<style>
    body { background: #1a120e; color: #ffb74d; font-family: monospace; display: flex; flex-direction: column; height: 100vh; margin: 0; }
    .widget { border: 2px solid #8d6e63; margin: 10px; padding: 20px; border-radius: 12px; background: rgba(0,0,0,0.3); }
    .btn { background: #3e2723; color: #ffb74d; border: 1px solid #8d6e63; padding: 15px; text-decoration: none; text-align: center; display: block; margin: 10px; border-radius: 8px; }
</style></head>
<body>
    <div class="widget">
        <div style="font-size: 0.7rem;">FAI v2.2.2 🪵🪓</div>
        <div id="bal" style="font-size: 2.5rem; font-weight: bold;">0.0000</div>
        <div style="font-size: 0.8rem; opacity: 0.6;">FTC BALANCE</div>
    </div>
    <a href="games/icechain.html" class="btn">MINING NODE</a>
    <script src="system/api.js"></script>
    <script>
        const refresh = () => document.getElementById('bal').innerText = Finux.Wallet.get();
        window.addEventListener('balanceUpdate', refresh); refresh();
    </script>
</body></html>
EOF

echo ">> 2.2.2 KERNEL READY."
