import hashlib
import json
from functools import lru_cache

class OptimizedValidator:
    def __init__(self, genesis_config):
        self.genesis = genesis_config
        self.chain_id = genesis_config['protocol']['chainId']

    @lru_cache(max_num=1024)
    def fast_hash(self, block_data_str):
        """Uses LRU cache to skip recalculating known valid blocks."""
        return hashlib.sha256(block_data_str.encode()).hexdigest()

    def validate_integrity(self, chain):
        """Optimized loop using local variable caching."""
        prev_hash = "0"
        # Localize for speed inside loop
        verify = self.fast_hash
        
        for i, block in enumerate(chain):
            # Check Chain ID consistency
            if block.get('chainId') != self.chain_id:
                return False, f"Block {i}: Invalid Chain ID"

            # Reconstruct string for hash check
            content = json.dumps({k: v for k, v in block.items() if k != 'hash'}, sort_keys=True)
            actual_hash = verify(content)

            if block['hash'] != actual_hash:
                return False, f"Block {i}: Hash Mismatch"
            
            if i > 0 and block['previous_hash'] != prev_hash:
                return False, f"Block {i}: Broken Link"
            
            prev_hash = block['hash']
            
        return True, "Chain Verified"
