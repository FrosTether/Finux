Here is the official FrostPay Integration Documentation.
You can save this as docs/FrostPay_Integration.md in your repository. This guide allows third-party developers (or your future self) to integrate the Fiat-to-Frostcoin gateway into any app running on Finux OS.
❄️ FrostPay Gateway Integration Guide (v1.2)
FrostPay is the native bridge for the Frost Protocol. It allows applications to accept standard Fiat payments (USD via Google Pay/Stripe) and automatically settlement in Frostcoin ($FTC) on the blockchain.
1. Architecture Overview
FrostPay acts as an oracle between the traditional banking system (Web2) and the Sovereign Frost Chain (Web3).
The Flow:
 * Client: App generates a payment session (Stripe) with the user's wallet_address attached as metadata.
 * Payment: User pays via Google Pay.
 * Webhook: Stripe notifies the FrostPay Bridge.
 * Minting: The Bridge verifies the payment and triggers the Treasury Smart Contract.
 * Settlement: $FTC tokens are minted directly to the user's wallet.
2. Quick Start
Prerequisites
 * Finux OS (v1.2 or higher)
 * Python 3.10+
 * API Keys: Stripe Secret Key, Webhook Secret, Frost Protocol Treasury Key.
Installation
pip install frostpay-sdk stripe web3

3. Client-Side Integration (Python/Finux)
Use this code in your app (Virgo_Wallet.py or similar) to initiate a transaction.
import webbrowser
import requests

def initiate_frost_payment(wallet_address, amount_usd):
    """
    Opens the FrostPay Secure Sheet for the user.
    """
    # 1. Request a Session from your Backend
    response = requests.post("https://api.frost-protocol.io/create-session", json={
        "amount": amount_usd,
        "wallet": wallet_address
    })
    
    if response.status_code == 200:
        checkout_url = response.json()['url']
        # 2. Launch Google Pay
        print(f"❄️ Initiating Transaction for ${amount_usd}...")
        webbrowser.open(checkout_url)
    else:
        print("❌ Error creating payment session.")

4. Server-Side Configuration
The FrostPay Bridge listens for successful payments. You must configure your environment variables for security.
| Variable | Description |
|---|---|
| STRIPE_SECRET_KEY | Your private Stripe key (sk_...) |
| STRIPE_WEBHOOK_SECRET | The signing secret for your webhook endpoint (whsec_...) |
| TREASURY_KEY | Private Key of the wallet authorized to Mint FTC |
| CONTRACT_ADDRESS | Address of the deployed FrostToken.sol |
Webhook Verification Logic
The bridge automatically handles the exchange rate (currently 1 USD = 10 FTC).
# The logic inside FrostPay_Bridge.py
tokens_to_mint = amount_paid_usd * 10
contract.functions.mint(user_wallet, tokens_to_mint).transact()

5. Testing & Dev Mode
To test your integration without spending real money, you can use Dev Mode. This bypasses the Stripe cryptographic signature check.
Command to Mock a Payment:
curl -X POST http://localhost:5000/webhook \
     -H "Content-Type: application/json" \
     -H "X-Dev-Mode: true" \
     -d '{
           "type": "checkout.session.completed",
           "data": {
             "object": {
               "amount_total": 5000,
               "metadata": { "wallet_address": "0xTEST_WALLET" }
             }
           }
         }'

Expected Response:
{
  "success": true,
  "minted": 500.0,
  "status": "MINT_INITIATED"
}

6. Smart Contract Reference
 * Network: Frost Chain (Chain ID: 9921)
 * Token Standard: ERC-20 (Burnable, Mintable)
 * Access Control: Only addresses with MINTER_ROLE can trigger the gateway.
Would you like me to create the deploy_docs.sh script to publish this Markdown file to your GitHub Wiki page automatically?
