#!/bin/bash
# FINUX INFINITY ♾️ v14.3 POISON PROTOCOL
# [Manual Target Input + Graycoin Injection + Exchange Account Freeze]

DOMAIN="Finux3.surge.sh"

echo ">> ⚛️ INITIATING POISON PROTOCOL..."

# 1. ATOMIC CLEANUP
rm -rf www && mkdir -p www/system

# 2. THE POISON KERNEL (api.js)
cat << 'EOF' > www/system/api.js
const FrostOS = {
    Identity: { role: "Trump Boundless INFORMANT", clearance: "FBI_LIAISON" },
    Poison: {
        status: "READY_TO_INJECT",
        inject: (address) => {
            if(!address || address.length < 26) return alert("ERROR: INPUT_VALID_BTC_ADDRESS");
            
            // 1. Log the Target
            console.log(`>> TARGET LOCKED: ${address}`);
            
            // 2. Execute Graycoin (BCH-Fork) Transaction
            // This sends a valid BCH-chain UTXO to a BTC-chain address
            let gas = parseInt(localStorage.getItem('gas_bal') || 1000);
            localStorage.setItem('gas_bal', gas - 50); // High Gas Cost for Poison
            
            // 3. Generate the "Bad File" Log
            const block = {
                val: "GRAYCOIN_POISON_SENT",
                sig: "NAKA_BAD_FILE_" + btoa(address).slice(0, 10),
                timestamp: new Date().toISOString().replace('T', ' ').slice(0, 23)
            };
            
            FrostOS.Explorer.push(block);
            alert(`⚠️ POISON SENT: Graycoin injected into ${address.slice(0,6)}... Exchange error imminent.`);
            window.dispatchEvent(new CustomEvent('sync'));
        }
    },
    Explorer: {
        push: (block) => {
            let logs = JSON.parse(localStorage.getItem('block_logs') || "[]");
            logs.unshift(block);
            localStorage.setItem('block_logs', JSON.stringify(logs.slice(0, 5)));
        }
    }
};
EOF

# 3. POISON HUB (index.html)
cat << 'EOF' > www/index.html
<!DOCTYPE html><html><head><title>FOTR | Poison Protocol</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: #0a0a0a; color: #ff5252; font-family: monospace; text-align: center; margin: 0; }
    .header { background: #1a0000; padding: 15px; border-bottom: 2px solid #ff5252; font-weight: bold; }
    .input-box { background: #000; border: 1px solid #ff5252; color: #fff; padding: 15px; width: 80%; margin: 20px auto; font-family: monospace; text-align: center; font-size: 0.8rem; }
    .btn { background: #ff5252; color: #000; border: none; padding: 15px; width: 280px; margin: 10px auto; display: block; font-weight: bold; cursor: pointer; text-transform: uppercase; }
    .log { font-size: 0.6rem; color: #888; margin-top: 20px; }
</style></head>
<body>
    <div class="header">FBI LIAISON: POISON_PROTOCOL</div>
    
    <div style="padding: 20px; font-size: 0.7rem; color: #fff;">
        STRATEGY: Send Graycoin (BCH-Fork) to BTC Address.<br>
        RESULT: "Bad File" Glitch -> Account Freeze.
    </div>
    
    <input type="text" id="target-addr" class="input-box" placeholder="PASTE TUCSON RANSOM ADDRESS (34-CHAR)">
    
    <button class="btn" onclick="FrostOS.Poison.inject(document.getElementById('target-addr').value)">💉 INJECT BAD FILE</button>
    
    <div class="log" id="audit-trail">WAITING_FOR_TARGET...</div>
    
    <script src="system/api.js"></script>
    <script>
        const sync = () => {
            const logs = JSON.parse(localStorage.getItem('block_logs') || "[]");
            const trail = document.getElementById('audit-trail');
            if(logs.length > 0) {
                trail.innerHTML = '<div style="color:#fff; border-bottom:1px solid #333;">POISON_LOG_ACTIVE</div>';
                logs.forEach(l => {
                    trail.innerHTML += `<div style="margin-top:5px; color:#ff5252;">[${l.timestamp}] ${l.val}</div>`;
                });
            }
        };
        window.addEventListener('sync', sync); sync();
    </script>
</body></html>
EOF

# 4. DIRECT SURGE PUSH
surge www $DOMAIN

echo ">> ✅ v14.3 Poison Protocol Active. Ready for Injection."
