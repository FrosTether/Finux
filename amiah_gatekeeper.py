import hashlib
import json
from fros_tether_core import Wallet

class Gatekeeper:
    def __init__(self, ledger):
        self.ledger = ledger
        self.genesis_string = "YOUR_TATTOO_GENESIS_STRING_HASH" # The Master Key

    def generate_invite(self, voucher_wallet):
        """Creates a cryptographically signed Invite Ticket."""
        invite_payload = {
            "voucher": voucher_wallet.identity,
            "timestamp": time.time(),
            "type": "STANDARD_INVITE"
        }
        # Sign the payload to prove it came from a trusted node
        signature = voucher_wallet.sign_message(json.dumps(invite_payload))
        ticket = f"{voucher_wallet.identity}:{signature}"
        
        print(f"🎟️ Invite Ticket Generated for {voucher_wallet.identity}")
        print(f"Code: {ticket}")
        return ticket

    def register_user(self, new_user_pubkey, invite_ticket, tattoo_proof=None):
        """The Gatekeeper: Validates entry via Ticket OR Tattoo."""
        
        # PATH A: The "Tattoo" Bypass (Master Override)
        if tattoo_proof and self.verify_tattoo(tattoo_proof):
            print(f"❄️ TATTOO VERIFIED. Bypassing Invite for {new_user_pubkey}")
            return self.create_account(new_user_pubkey, status="ELITE")

        # PATH B: The "Vouch" (Standard Entry)
        voucher_id, signature = invite_ticket.split(":")
        if self.ledger.get_reputation(voucher_id) > 50: # Only trusted users can invite
            if self.verify_signature(voucher_id, signature):
                print(f"✅ Vouch Accepted. {voucher_id} -> {new_user_pubkey}")
                return self.create_account(new_user_pubkey, status="MEMBER")
        
        print("⛔ ACCESS DENIED: Invalid Invite or Low Reputation.")
        return False

    def verify_tattoo(self, proof):
        """Checks if the submitted string matches the Genesis Hash."""
        return hashlib.sha256(proof.encode()).hexdigest() == self.genesis_string
