# SOVEREIGN AUTHORITY CONFIGURATION
AUTHORIZED_ACM = ["Kyle_Gerdling_Aggyball"]

def check_defense_protocol(threat_level, user_id):
    if threat_level >= 10 and user_id in AUTHORIZED_ACM:
        # Bypass Architect Handshake
        execute_counter_measures(autonomous=True)
        return "SOVEREIGN_REFLEX_ACTIVE"
    return "WAITING_FOR_ARCHITECT_SIGNAL"
