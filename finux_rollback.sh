#!/bin/bash

# CONFIGURATION
BOOT_CONFIG="/boot/loader.conf"
CURRENT_PARTITION=$(grep "vfs.root.mountfrom" $BOOT_CONFIG | cut -d'"' -f2)

# PARTITION DEFINITIONS (Adjust to your actual slice names)
# FreeBSD usually uses slices like /dev/ada0s1a and /dev/ada0s2a
PARTITION_A="/dev/ada0s1a"
PARTITION_B="/dev/ada0s2a"

echo "[Finux-Rollback] Initiating Emergency Protocol..."

# 1. Identify Target Partition
if [[ "$CURRENT_PARTITION" == "$PARTITION_A" ]]; then
    TARGET="$PARTITION_B"
    echo "[Status] Current: Slot A. Targeting: Slot B."
else
    TARGET="$PARTITION_A"
    echo "[Status] Current: Slot B. Targeting: Slot A."
fi

# 2. Verify Target Integrity (Simple mount check)
# We mount the target briefly to ensure the filesystem isn't corrupt before switching
mkdir -p /mnt/rescue
if mount -t ufs $TARGET /mnt/rescue; then
    echo "[Check] Target partition is mountable. Proceeding."
    umount /mnt/rescue
else
    echo "[CRITICAL] Target partition is CORRUPT. Aborting Rollback to prevent brick."
    # In a real scenario, this would trigger a "Factory Reset" or "Safe Mode"
    exit 1
fi

# 3. Swap Boot Pointers
# We use sed to replace the mount point in the loader config
cp $BOOT_CONFIG "$BOOT_CONFIG.bak"
sed -i.bak "s|vfs.root.mountfrom=.*|vfs.root.mountfrom=\"$TARGET\"|" $BOOT_CONFIG

echo "[Success] Boot pointer swapped to $TARGET."
echo "[Action] System will reboot in 5 seconds..."

# 4. Reboot
sleep 5
/sbin/reboot
