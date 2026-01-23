import secrets
import json

def generate_guardian_invitation(user_id, guardian_name):
    """
    Creates a secure invitation for a guardian to join the recovery network.
    """
    # 1. Generate a unique invitation token
    invitation_token = secrets.token_urlsafe(32)
    
    # 2. Package the invitation data
    invitation_data = {
        "from": user_id,
        "to": guardian_name,
        "token": invitation_token,
        "expires": "48h",
        "action": "DECENTR_RECOVERY_ENROLL"
    }
    
    # 3. Create the encrypted link (Conceptual)
    invite_link = f"https://graysonswallet.io/invite?data={invitation_token}"
    
    message = (
        f"Hey {guardian_name}, I'm setting up a secure recovery for Grayson's Wallet. "
        f"Would you be willing to be a Guardian? You won't see my keys, but you can "
        f"help me verify my identity if I ever lose my phone. Link: {invite_link}"
    )
    
    return message

# Example: generate_guardian_invitation("Jacob_Frost", "Kelsee")
