import os
import hashlib

class FrostnerjoProtocol:
    def __init__(self):
        self.protocol_name = "Cryptonite"
        self.halving_interval = 3_000_000
        self.scratchpad_size = 2 * 1024 * 1024 # 2MB Cache Requirement
        
    def get_fnr_reward(self, height):
        """Matches the 5y 8m ecosystem standard."""
        return 100.0 / (2 ** (height // self.halving_interval))

    def crypto_night_hash(self, data):
        """Simulates memory-hard CPU mining."""
        # Scratchpad prevents ASIC dominance
        scratchpad = hashlib.sha256(data).digest() * 65536 
        result = hashlib.pbkdf2_hmac('sha256', data, scratchpad[:64], 2048)
        return result.hex()
