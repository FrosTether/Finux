# 1. Install the missing 'make' and 'rust' tools from your 4926/4932 errors
pkg install build-essential make rust clang -y

# 2. Re-install the Kraken SDK now that Rust is present
pip install maturin setuptools wheel python-kraken-sdk

# 3. Create and launch the authorized Newkirk script
cat << 'EOF' > launch_protocol.sh
#!/bin/bash
echo "🛡️  [NEWKIRK OVERRIDE] Virgo ♍ x1777 Active"
python3 kelsee_dashboard.py
EOF

chmod +x launch_protocol.sh
./launch_protocol.sh
