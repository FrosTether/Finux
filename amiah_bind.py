import steem
from steem.account import Account

def bind_nft_to_steem(doodle_id, owner_account):
    """Binds an amiahdoodles NFT to a Steem.it core account."""
    s = steem.Steem()
    
    # Dogecoin Principle: Only Good Everyday (Charity Tax)
    charity_share = 0.10 # 10% of rewards go to community fund
    
    metadata = {
        "nft_id": doodle_id,
        "principles": "Do Only Good Everyday",
        "backing": "amiah.do ecosystem",
        "charity_tax": charity_share
    }
    
    # Broadcast the 'backing' link to the Steem blockchain
    s.commit.custom_json(
        id="amiahdo_nft_bind",
        json_data=metadata,
        required_posting_auths=[owner_account]
    )
    print(f"✅ NFT {doodle_id} now backed by Steem.it core for @{owner_account}")
