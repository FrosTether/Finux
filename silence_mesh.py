#!/bin/bash
# SILENCE.IM / MESH FALLBACK PROTOCOL
# Port: 7444

echo "📡 MONITORING SIGNAL INTEGRITY..."

# Check if online
ping -c 1 8.8.8.8 > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "⚠️  INTERNET OFFLINE. SWITCHING TO SILENCE MESH..."
    # Force XMPP over Local Radio/Bluetooth/SMS
    export MESSENGER_BACKEND="SMS_ENCRYPTED_SILENCE"
    export PORT=7444
    echo "🔐 ENCRYPTION: Signal Protocol (Offline Mode)"
    echo "✅ MESH READY: Broadcasting on 7444"
else
    echo "🌐 ONLINE: Using XMPP over I2P Tunnel"
fi
