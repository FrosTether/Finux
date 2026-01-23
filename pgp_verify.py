import gnupg
import os

# Initialize GnuPG
gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

def create_identity_signature(email):
    """Generates a signed message to prove identity."""
    message = f"I, Jacob Frost, am the rightful owner of @agorajay. Contact: {email}"
    
    # Sign the message using your private key
    signed_data = gpg.sign(message, clearsign=True)
    
    if signed_data.status == "signature created":
        with open('frost_identity_proof.asc', 'w') as f:
            f.write(str(signed_data))
        print(f"✅ Identity Proof generated for {email}. Share the .asc file with the community.")
    else:
        print("❌ Error: PGP key not found for this email.")

# Run for your new primary contact
if __name__ == "__main__":
    create_identity_signature("voluntaryistj@riseup.net")
