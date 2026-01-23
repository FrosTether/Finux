# Conceptual logic for adding a secondary 'Guardian' device
def add_guardian_device(primary_user_id, secondary_pub_key):
    """
    Registers a secondary hardware-backed key to assist in recovery.
    """
    # 1. Primary device biometrically authorizes the addition
    # 2. Secondary public key is stored on the bridge backend
    bridge_backend.register_guardian(primary_user_id, secondary_pub_key)
    print("Backup device linked successfully.")
