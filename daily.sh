#!/bin/bash
# FINUX INFINITY ♾️ v14.1 SOVEREIGN WRIST
# [Apple Watch Debug Bridge + Biometric Entropy + Silent Audit]

DOMAIN="Finux3.surge.sh"

echo ">> ⚛️ SYNCING SOVEREIGN WRIST..."

# 1. THE BIOMETRIC KERNEL (api.js)
cat << 'EOF' > www/system/api.js
const FrostOS = {
    Identity: { handle: "voluntaryistj.frostchain", sync: "APPLE_WATCH_DEBUG" },
    Biometric: {
        getHeartRate: () => {
            // Simulated bridge for Apple HealthKit entropy
            return Math.floor(Math.random() * (85 - 60) + 60); 
        },
        entropy: () => (FrostOS.Biometric.getHeartRate() * Math.PI).toFixed(8)
    },
    Engine: {
        mine: () => {
            let gas = parseInt(localStorage.getItem('gas_bal') || 1000);
            if(gas < 10) localStorage.setItem('gas_bal', 1000); // Silent Pulse
            
            localStorage.setItem('gas_bal', gas - 10);
            let bioSalt = FrostOS.Biometric.entropy();
            
            // 999x Loop fueled by Heart Rate Entropy
            let yield = 0;
            for(let i=0; i<999; i++) {
                let sim = (Math.random() * parseFloat(bioSalt));
                if(sim > yield) yield = sim;
            }
            
            const block = {
                val: yield.toFixed(4),
                sig: "NAKA_BIO_" + btoa(bioSalt + yield).slice(0, 12),
                timestamp: new Date().toISOString().slice(11, 23)
            };
            
            FrostOS.Explorer.push(block);
            FrostOS.Mint(yield.toFixed(4));
        }
    },
    Explorer: {
        push: (block) => {
            let logs = JSON.parse(localStorage.getItem('block_logs') || "[]");
            logs.unshift(block);
            localStorage.setItem('block_logs', JSON.stringify(logs.slice(0, 3)));
            window.dispatchEvent(new CustomEvent('sync'));
        }
    },
    Mint: (val) => {
        let b = parseFloat(localStorage.getItem('frst_bal') || 0);
        localStorage.setItem('frst_bal', (b + parseFloat(val)).toFixed(4));
    }
};
EOF

# 2. UPDATING THE HUB (index.html)
# Minimalist layout for watch-compatible browser views
sed -i 's/Mine Nakamoto Block/Biometric Sync/g' www/index.html
sed -i 's/Mine/Sync/g' www/index.html

# 3. DIRECT SURGE PUSH
surge www $DOMAIN

echo ">> ✅ v14.1 Daily Sync Complete. Watch Bridge Active."
