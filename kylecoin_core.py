import hashlib
import time

class KylecoinProtocol:
    def __init__(self):
        self.halving_interval = 3_000_000  # 5 Years, 8 Months
        self.initial_reward = 50.0        # KYLE per block
        self.block_time_target = 60       # Seconds
        
    def get_current_reward(self, block_height):
        """Calculates reward based on the 5y 8m cycle."""
        halvings = block_height // self.halving_interval
        if halvings >= 33: # Max supply reached
            return 0
        return self.initial_reward / (2 ** halvings)

    def validate_mining(self, block_height, score, difficulty):
        """Standard CPU Proof-of-Work validation."""
        reward = self.get_current_reward(block_height)
        # Mining logic here
        return reward
