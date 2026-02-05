#!/bin/bash
# FINUX INFINITY ♾️ v7.2 CLEAN SLATE
# [Structural Purge + Citizen Profile + Amiah Integration]

DOMAIN="Finux3.surge.sh"

echo ">> ♾️ INITIATING STRUCTURAL PURGE..."

# 1. TOTAL WIPE & RECONSTRUCT (Deleting old crush.html and ghost files)
rm -rf www
mkdir -p www/system www/assets/images

# 2. SOVEREIGN API (The Omni-Kernel)
cat << 'EOF' > www/system/api.js
const FrostOS = {
    Identity: {
        handles: ["voluntaryistj.base.eth", "1cnjacobfrost.blockchain", "voluntaryistj.frostchain"],
        name: "Jacob Frost",
        github: "FrosTether",
        compliance: "FrostPlat_Standard_v1"
    },
    Economy: {
        mint: (units) => {
            let fh = parseInt(localStorage.getItem('fh_bal') || 0);
            localStorage.setItem('fh_bal', fh + units);
            window.dispatchEvent(new CustomEvent('sync'));
        }
    }
};
EOF

# 3. CITIZEN PROFILE (system/profile.html)
cat << 'EOF' > www/system/profile.html
<!DOCTYPE html><html><head><title>Citizen Profile | Jacob Frost</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: #000; color: #fff; font-family: monospace; text-align: center; padding: 20px; }
    .profile-card { border: 2px solid #81c784; background: rgba(129, 199, 132, 0.05); padding: 30px; border-radius: 20px; max-width: 400px; margin: auto; }
    .doodle { width: 150px; border-radius: 50%; border: 3px solid #81c784; margin-bottom: 20px; }
    .label { color: #81c784; font-size: 0.7rem; margin-top: 15px; }
    .val { font-size: 1.1rem; border-bottom: 1px solid #333; padding-bottom: 5px; }
</style></head>
<body>
    <div class="profile-card">
        <img src="../assets/images/amiah_doodle.png" class="doodle">
        <h2>SOVEREIGN CITIZEN</h2>
        <div class="label">LEGAL NAME</div><div class="val">Jacob Frost</div>
        <div class="label">GITHUB</div><div class="val">FrosTether</div>
        <div class="label">PRIMARY HANDLE</div><div class="val">voluntaryistj.frostchain</div>
    </div>
    <br><a href="../index.html" style="color:#81c784;">[ RETURN TO HUB ]</a>
</body></html>
EOF

# 4. THE CLEAN OMNI-HUB (index.html)
cat << 'EOF' > www/index.html
<!DOCTYPE html><html><head><title>voluntaryistj.frostchain</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    body { background: radial-gradient(circle, #1a1a1a 0%, #000 100%); color: white; font-family: monospace; text-align: center; margin: 0; padding: 20px; }
    .stable-card { background: rgba(255, 255, 255, 0.05); border: 2px solid #fff; border-radius: 15px; padding: 25px; margin-bottom: 20px; }
    .btn { background: #3e2723; border: 1px solid #ffb74d; color: #ffb74d; padding: 15px; text-decoration: none; border-radius: 8px; display: block; margin: 10px auto; font-weight: bold; width: 220px; }
</style></head>
<body>
    <div style="font-size: 0.7rem; color: #81c784; margin-bottom: 20px;">NODE: voluntaryistj.frostchain</div>
    
    <div class="stable-card">
        <div style="font-size: 2.8rem; font-weight: 900;" id="fh-bal">$0.00</div>
        <div style="font-size: 0.7rem; letter-spacing: 2px; opacity: 0.7;">FROSTHASH STABLE UNITS</div>
    </div>

    <a href="system/profile.html" class="btn">👤 CITIZEN PROFILE</a>
    <a href="system/registry.html" class="btn">📜 SEC REGISTRY</a>
    
    <script>
        const sync = () => {
            let pennies = parseInt(localStorage.getItem('fh_bal') || 0);
            document.getElementById('fh-bal').innerText = "$" + (pennies / 100).toFixed(2);
        };
        window.addEventListener('focus', sync); sync();
    </script>
</body></html>
EOF

# 5. RESTORE CRITICAL ASSETS ONLY
# Re-generating the Amiah Doodle for the Profile
python3 -c "from PIL import Image, ImageDraw; img = Image.new('RGBA', (512, 512), (255, 255, 255, 0)); draw = ImageDraw.Draw(img); draw.ellipse([50, 50, 462, 462], fill=(200, 230, 255, 255), outline=(129, 199, 132), width=15); img.save('www/assets/images/amiah_doodle.png')"

# 6. DIRECT SURGE PUSH
surge www $DOMAIN

echo ">> ✅ Structure Purged and Fixed. Legacy Files Deleted."
