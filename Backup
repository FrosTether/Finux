#!/bin/bash

# --- MONOKILLER COLD-STORAGE BACKUP ---
# Target: Encrypted External Drive
# Protocol: 1.3.37 / Virgo x1777

# 1. Define Paths
SOURCE_DIR=$(pwd)
BACKUP_DATE=$(date +%Y-%m-%d)
BACKUP_NAME="Frostnerjo_Sovereign_Backup_$BACKUP_DATE.tar.gz"

echo "🔱 [BACKUP] Detecting external drive..."
read -p "Enter the Path to External Drive (e.g. /Volumes/USB): " DRIVE_PATH

if [ ! -d "$DRIVE_PATH" ]; then
    echo "❌ ERROR: External drive not found at $DRIVE_PATH"
    exit 1
fi

# 2. Package the Protocol
echo "📦 [PACKAGING] Compressing source code and metadata..."
tar -czf "$BACKUP_NAME" .env monokiller_validator.py kelsee_dashboard.py kelsee_settle.py README.md .gitignore

# 3. Encrypt the Archive
echo "🔐 [ENCRYPTING] Encrypting with GPG..."
gpg -c --cipher-algo AES256 "$BACKUP_NAME"

# 4. Secure Transfer
echo "💾 [TRANSFERRING] Moving to Cold Storage..."
mv "$BACKUP_NAME.gpg" "$DRIVE_PATH/"
rm "$BACKUP_NAME" # Delete the unencrypted local zip

echo "---"
echo "✅ [SUCCESS] Sovereign Backup Saved to: $DRIVE_PATH"
echo "🔐 [NOTE] The file is now encrypted. Kelsee will need the GPG passphrase to recover it."
