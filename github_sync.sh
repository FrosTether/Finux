cat <<EOF > github_sync.sh
#!/bin/bash
# 1. Locate the forged APK
APK_FILE=\$(find bin/ -name "*.apk" | head -n 1)

if [ -f "\$APK_FILE" ]; then
    echo "--- Artifact Found: \$APK_FILE ---"
    
    # 2. Commit the new build to FrosTether/Finux
    git add .
    git commit -m "Automated Forge: FNR Miner signed with Birth UTC"
    git push origin main
    
    echo "--- Push Successful to GitHub ---"
else
    echo "Error: No APK found. Forge might still be running."
fi
EOF

chmod +x github_sync.sh
