# Masternode Persistence Script
while true; do
  # Check if Frosku is the active app
  STATUS=$(curl -s http://192.168.0.2:8060/query/active-app | grep "dev")
  if [ -z "$STATUS" ]; then
    echo "⚠️ [MASTERNODE] Frosku Offline. Re-initiating God Code..."
    curl -d '' -s "http://192.168.0.2:8060/launch/dev"
    # Auto-maximize Volume for the 87-year-old safety check
    for i in {1..5}; do curl -d '' -s http://192.168.0.2:8060/keypress/VolumeUp; done
  fi
  sleep 60 # Check every minute
done
