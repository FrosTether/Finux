import hashlib
import time
import json
import ipfshttpclient  # Requires: pip install ipfshttpclient
from fros_tether_core import FrostBlock, Wallet  # Importing your V1.1 Core

class AmiahSocialNode:
    def __init__(self, node_id, wallet):
        self.node_id = node_id
        self.wallet = wallet
        self.ipfs = ipfshttpclient.connect()
        self.reward_pool = 100000.00  # Daily FTC inflation pool
        self.pending_posts = []

    def submit_doodle(self, image_path, caption, tags):
        """Uploads Doodle to IPFS and broadcasts the hash to Frost Protocol."""
        print(f"❄️ Uploading {image_path} to Decentralized Web...")
        
        # 1. Store Content on IPFS (The 'Steem' Model)
        res = self.ipfs.add(image_path)
        ipfs_hash = res['Hash']
        
        # 2. Create the Post Object
        post = {
            "author": self.wallet.identity,  # voluntaryist.base.eth
            "permlink": f"amiah-doodle-{int(time.time())}",
            "ipfs_cid": ipfs_hash,
            "caption": caption,
            "tags": tags,
            "taps": 0,  # "Taps" = Upvotes
            "timestamp": time.time()
        }
        
        # 3. Sign and Broadcast
        signature = self.wallet.sign_message(json.dumps(post))
        post['sig'] = signature
        self.pending_posts.append(post)
        
        print(f"✅ Doodle Launched! IPFS Hash: {ipfs_hash}")
        print(f"🔗 Viewable at: https://ipfs.io/ipfs/{ipfs_hash}")
        return post

    def tap_it_out(self, post_permlink, voter_weight):
        """The 'Tap' Mechanism (Voting)."""
        # In Steem, 1 Tap = 1 Vote weighted by Frost Power (FP)
        print(f"👆 Tapping {post_permlink} with {voter_weight}% Power...")
        # Logic to record vote in memory pool...

    def process_rewards(self):
        """Runs every 24h. Distributes FTC from Reward Pool."""
        # Steem Algorithm: 75% to Author, 25% to Curators (Tappers)
        print("💰 Calculating Viral Rewards...")
        for post in self.pending_posts:
            if post['taps'] > 0:
                payout = (post['taps'] / self.total_network_taps) * self.reward_pool
                author_share = payout * 0.75
                curator_share = payout * 0.25
                print(f"  > {post['permlink']}: {author_share:.2f} FTC to Author")

# Initialize the Social Node
node = AmiahSocialNode("Monroeville-01", local_wallet)
