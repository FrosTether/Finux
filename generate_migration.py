import hashlib
import time
import json

class MigrationBlock:
    def __init__(self, index, previous_hash, migration_data):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.migration_data = migration_data
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty=4):
        """Standard PoW to secure the migration."""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()
        return self.hash

# Migration Data: Binding Legacy to Kraken
legacy_snapshot = {
    "source": "1cnjacobfrost.blockchain",
    "destination": "334BSEeNo9wMhASUH9tCA7CKCMKuuARyRg",
    "verified_by": "voluntaryist.base.eth",
    "legacy_password_status": "RECOVERED",
    "principles": "DOGE (Do Only Good Everyday)"
}

# Generate Block #1
genesis_hash = "0000888frost_genesis_hash_placeholder" # From Block #0
migration_block = MigrationBlock(1, genesis_hash, legacy_snapshot)
migration_block.mine_block()

print(f"✅ Migration Block #1 Generated!")
print(f"Hash: {migration_block.hash}")
