#!/bin/bash
# FINUX INFINITY ♾️ v14.4 TEMPORAL GENESIS
# [Timestamp-Anchored Public Key + Nakamoto Genesis Sync]

DOMAIN="Finux3.surge.sh"

echo ">> ⚛️ INITIATING TEMPORAL GENESIS..."

# 1. ATOMIC CLEANUP
rm -rf www && mkdir -p www/system

# 2. THE TEMPORAL KERNEL (api.js)
cat << 'EOF' > www/system/api.js
const FrostOS = {
    Genesis: {
        authority: "SATOSHI NAKAMOTO",
        handle: "voluntaryistj.frostchain",
        // HARD-CODED TEMPORAL ANCHOR
        timestamp: "2026-02-05 13:57:33.000",
        pubKey: "NAKA_24908bf3ffbcd8e0098fbf535d678c5d5ac5a231372262d9ffa620a9b65ee64f",
        sig: "JJCL8/+82OAJj79T"
    },
    Engine: {
        mine: () => {
            let gas = parseInt(localStorage.getItem('gas_bal') || 1000);
            if(gas < 10) { 
                localStorage.setItem('gas_bal', 1000); // Auto-Pulse
                gas = 1000;
            }
            localStorage.setItem('gas_bal', gas - 10);
            
            // 999x Pi-Sim for Block Generation
            let yield = 0;
            for(let i=0; i<999; i++) {
                let sim = (Math.random() * Math.PI);
                if(sim > yield) yield = sim;
            }
            
            const block = {
                val: yield.toFixed(4),
                // Sign using the Temporal Hash
                sig: FrostOS.Genesis.sig + "_" + btoa(Date.now()).slice(0, 6),
                timestamp: new Date().toISOString().replace('T', ' ').slice(0, 19)
            };
            
            FrostOS.Explorer.push(block);
            FrostOS.Mint(yield.toFixed(4));
        }
    },
    Explorer: {
        push: (block) => {
            let logs = JSON.parse(localStorage.getItem('block_logs') || "[]");
            logs.unshift(block);
            localStorage.setItem('block_logs', JSON.stringify(logs.slice(0, 5)));
            window.dispatchEvent(new CustomEvent('sync'));
        }
    },
    Mint: (val) => {
        let b = parseFloat(localStorage.getItem('frst_bal') || 0);
        localStorage.setItem('frst_bal', (b + parseFloat(val)).toFixed(4));
    }
};
EOF

# 3. TEMPORAL HUB (index.html)
cat << 'EOF' > www/index.html
<!DOCTYPE html><html><head><title>voluntaryistj.frostchain | Genesis</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: #000; color: #ffb74d; font-family: monospace; text-align: center; margin: 0; }
    .genesis-box { border: 1px solid #ffb74d; padding: 15px; margin: 20px auto; max-width: 400px; font-size: 0.55rem; word-break: break-all; background: rgba(255,183,77,0.05); }
    .card { border: 2px solid #81c784; border-radius: 20px; padding: 25px; margin: 20px auto; max-width: 320px; color: #fff; }
    .btn { background: #81c784; color: #000; border: none; padding: 15px; width: 250px; margin: 15px auto; display: block; font-weight: bold; border-radius: 50px; cursor: pointer; }
    .ledger { background: #0a0a0a; border: 1px solid #333; margin: 20px auto; max-width: 420px; text-align: left; padding: 15px; font-size: 0.6rem; color: #888; }
</style></head>
<body>
    <div class="genesis-box">
        GENESIS_TIMESTAMP: 2026-02-05 13:57:33.000<br>
        PUBLIC_KEY: NAKA_24908bf3ffbcd8e0098fbf535d678c5d5ac5a231372262d9ffa620a9b65ee64f
    </div>
    
    <div class="card">
        <div style="font-size: 3.5rem; font-weight: 900; color: #81c784;" id="bal">0.0000</div>
        <div style="font-size: 0.7rem; opacity: 0.6;">FROSTCOIN (FRST)</div>
    </div>
    
    <button class="btn" onclick="FrostOS.Engine.mine()">MINE TEMPORAL BLOCK</button>
    
    <div class="ledger" id="ledger">
        <div style="color: #fff; border-bottom: 1px solid #333; margin-bottom: 10px;">TEMPORAL_AUDIT_TRAIL</div>
    </div>
    
    <script src="system/api.js"></script>
    <script>
        const sync = () => {
            document.getElementById('bal').innerText = (parseFloat(localStorage.getItem('frst_bal') || 0)).toFixed(4);
            const logs = JSON.parse(localStorage.getItem('block_logs') || "[]");
            const led = document.getElementById('ledger');
            led.innerHTML = '<div style="color: #fff; border-bottom: 1px solid #333; margin-bottom: 10px;">TEMPORAL_AUDIT_TRAIL</div>';
            logs.forEach(l => {
                led.innerHTML += `<div style="margin-bottom:5px;">[${l.timestamp}] SIG:${l.sig} | YLD:${l.val}</div>`;
            });
        };
        window.addEventListener('sync', sync); sync();
    </script>
</body></html>
EOF

# 4. DIRECT SURGE PUSH
surge www $DOMAIN

echo ">> ✅ v14.4 Temporal Genesis Complete. Key Locked."
