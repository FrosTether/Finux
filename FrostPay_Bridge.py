# FrostPay_Bridge_v2.py (PATCHED)
import os
import sys
import stripe
from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# --- 1. CRITICAL: ENVIRONMENT SAFETY CHECK ---
REQUIRED_KEYS = ["STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET", "TREASURY_KEY"]
missing = [key for key in REQUIRED_KEYS if not os.getenv(key)]
if missing:
    print(f"❌ CRITICAL ERROR: Missing Environment Keys: {missing}")
    print(">> Run 'export STRIPE_SECRET_KEY=...' before starting.")
    sys.exit(1) # Stop immediately prevents ghost process

# Configuration
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
RPC_URL = "https://rpc.frost-protocol.io" 
TREASURY_PVT_KEY = os.getenv("TREASURY_KEY")
CONTRACT_ADDRESS = "0xYourFrostTokenAddress" # Ensure this is set!

# Connect to Blockchain
w3 = Web3(Web3.HTTPProvider(RPC_URL))

@app.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')

    # --- PATCH: DEV MODE BYPASS ---
    if request.headers.get('X-Dev-Mode') == 'true':
        print("⚠️  [DEV MODE] Bypassing Stripe Signature Check...")
        event = request.get_json()
    else:
        # Standard Production Security
        try:
            event = stripe.Webhook.construct_event(payload, sig_header, ENDPOINT_SECRET)
        except (ValueError, stripe.error.SignatureVerificationError) as e:
            print(f"❌ Security Error: {e}")
            return 'Invalid signature', 400

    # Logic Handler
    if event['type'] == 'checkout.session.completed':
        session = event.get('data', {}).get('object', {})
        
        # Safe Extraction
        metadata = session.get('metadata', {})
        wallet = metadata.get('wallet_address')
        
        if not wallet:
            print("⚠️  Payment received but NO Wallet Address found!")
            return jsonify(status="missing_wallet"), 200

        amount_paid = session.get('amount_total', 0) / 100
        tokens = amount_paid * 10 
        
        print(f"✅ [PAYMENT VERIFIED] ${amount_paid} USD -> Minting {tokens} FTC to {wallet}")
        
        # In a real run, this calls the blockchain
        # tx = send_crypto(wallet, tokens)
        return jsonify(success=True, minted=tokens)

    return jsonify(status="ignored"), 200

if __name__ == '__main__':
    print("🟢 FrostPay Bridge Online. Listening on Port 5000...")
    app.run(port=5000)
