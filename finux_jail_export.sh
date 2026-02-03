#!/bin/sh
# ------------------------------------------------------------------
# FINUX PROVISIONER - FROST CRUSH MINING JAIL
# Author: DrFrostWavhz
# Kernel: Finux (FreeBSD 14.x Base)
# Purpose: Isolate 'Frost Crush' mining process in a secure container
# ------------------------------------------------------------------

# CONFIGURATION
JAIL_NAME="frost_crush"
JAIL_PATH="/usr/jails/${JAIL_NAME}"
FINUX_RELEASE="14.0-RELEASE" # Matching your Finux Base
IP_ADDR="10.0.0.5"           # Internal mesh IP
INTERFACE="lo1"              # Loopback clone for inter-jail comms

# Check for Root (Sovereignty Check)
if [ "$(id -u)" != "0" ]; then
   echo "This script requires Root/Sudo privileges. Access Denied."
   exit 1
fi

echo "[*] Initializing Finux Jail Protocol for: ${JAIL_NAME}..."

# 1. CREATE ZFS DATASET (Storage Layer)
# Finux uses ZFS for snapshotting the miner state.
echo "[*] Creating ZFS Dataset..."
zfs create -o mountpoint=${JAIL_PATH} zroot/jails/${JAIL_NAME}

# 2. BOOTSTRAP USERLAND (The OS inside the OS)
# Downloads/Installs the base Finux/BSD binaries into the jail folder.
echo "[*] Fetching Base System (base.txz)..."
bsdinstall jail ${JAIL_PATH}

# 3. CONFIGURE DEVFS (Hardware Access)
# The miner needs access to random number generators and crypto accelerators.
echo "[*] Configuring DevFS Rules..."
cat <<EOT >> /etc/devfs.rules
[devfs_rules_frost_miner=10]
add include $devfsrules_hide_all
add include $devfsrules_unhide_basic
add include $devfsrules_unhide_login
add path 'bpf*' unhide           # Network packet access for Mesh
add path 'crypto' unhide         # Hardware Crypto Acceleration
add path 'random' unhide         # RNG for Nonce generation
EOT

# 4. CONFIGURE JAIL.CONF (The Jail Logic)
# Defines how the jail runs on boot.
echo "[*] Registering Jail in /etc/jail.conf..."
cat <<EOT >> /etc/jail.conf
${JAIL_NAME} {
    # System Specs
    path = "${JAIL_PATH}";
    host.hostname = "${JAIL_NAME}.finux.local";
    
    # Network Isolation (VNET)
    ip4.addr = "${INTERFACE}|${IP_ADDR}/24";
    interface = "${INTERFACE}";
    
    # Permissions
    allow.raw_sockets = 1;       # Required for P2P Mining Mesh
    allow.sysvipc = 1;           # Inter-process communication
    
    # Security Rules
    devfs_ruleset = 10;          # Apply the 'frost_miner' rules above
    securelevel = 2;             # High security
    
    # Startup/Shutdown Scripts
    exec.start = "/bin/sh /etc/rc";
    exec.stop = "/bin/sh /etc/rc.shutdown";
}
EOT

# 5. INJECT MINING DAEMON (Placeholder)
# Creates the directory where the Proof-of-Crush logic will live.
mkdir -p ${JAIL_PATH}/usr/local/finux/frost_miner
echo "Active Session: Frost Crush" > ${JAIL_PATH}/usr/local/finux/frost_miner/status.log

# 6. ENABLE ON BOOT
sysrc jail_enable="YES"
sysrc jail_list+=" ${JAIL_NAME}"

# 7. LAUNCH
echo "[*] Freezing Jail... (Starting Service)"
service jail start ${JAIL_NAME}

echo "------------------------------------------------------------------"
echo "   [SUCCESS] Frost Crush Miner is now Active in Jail: ${IP_ADDR}"
echo "   Use 'jexec ${JAIL_NAME} /bin/csh' to enter the environment."
echo "------------------------------------------------------------------"
