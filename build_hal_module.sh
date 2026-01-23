#!/bin/bash

# Finux build script for Aluminium OS HAL (2026 Edition)
# Target: Diamond Tier Enterprise Security

TARGET_PLATFORM=${1:-"aluminium_2026"}
DRIVERS_DIR="./kernel/drivers/hal"
BUILD_DIR="./out/hal_build"

echo "--- Starting Finux HAL Build for: $TARGET_PLATFORM ---"

# 1. Environment Verification
if ! command -v aarch64-aluminium-gcc &> /dev/null; then
    echo "Error: Aluminium 2026 Toolchain not found. Please install 'al-sdk-1.0'."
    exit 1
fi

# 2. Frost Protocol Hook Injection
# This ensures the kernel requires a Frost signature for any HAL-level execution.
echo "Injecting Frost Protocol security hooks..."
python3 ./scripts/inject_frost_hooks.py --module=finux_hal_v1 --security-level=diamond

# 3. Compilation
# Compiling the AIDL-based interface for Aluminium OS
mkdir -p $BUILD_DIR
echo "Compiling AIDL interfaces for Finux..."
aarch64-aluminium-gcc $DRIVERS_DIR/finux_hal_core.c -o $BUILD_DIR/finux_hal.so \
    -I/usr/include/aluminium/hal \
    -L/usr/lib/aluminium/ase \
    -lase_security -lfrost_verify

# 4. Registration with ASE (Aluminium Secure Enclave)
if [ $? -eq 0 ]; then
    echo "Build Successful. Registering module with Secure Enclave..."
    ase-register --module=$BUILD_DIR/finux_hal.so --vendor="FrosTether"
    echo "--- Finux HAL Module Ready for Deployment ---"
else
    echo "Build Failed. Check kernel logs for HAL-AIDL mismatch."
    exit 1
fi
