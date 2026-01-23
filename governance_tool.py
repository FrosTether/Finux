import json
import os
from web3 import Web3

# --- CONFIGURATION ---
RPC_URL = "https://mainnet.base.org" 
PRIVATE_KEY = "YOUR_PRIVATE_KEY_HERE"  # <--- REMEMBER TO SET THIS

# --- LOAD CONTRACT ---
contract_path = "contract_data.json"
if not os.path.exists(contract_path):
    raise FileNotFoundError("Run deploy.py first!")

with open(contract_path, "r") as file:
    data = json.load(file)
    CONTRACT_ADDRESS = data["address"]
    CONTRACT_ABI = data["abi"]

w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)
account = w3.eth.account.from_key(PRIVATE_KEY)

def get_latest_proposal():
    """Fetches the latest proposal data for the GUI."""
    try:
        count = contract.functions.proposalCount().call()
        if count == 0:
            return {"id": 0, "desc": "No proposals yet", "for": 0, "against": 0}
            
        p = contract.functions.proposals(count).call()
        # Convert Wei to Ether for readability
        votes_for = w3.from_wei(p[2], 'ether')
        votes_against = w3.from_wei(p[3], 'ether')
        
        return {
            "id": p[0],
            "desc": p[1],
            "for": float(votes_for),
            "against": float(votes_against),
            "executed": p[4]
        }
    except Exception as e:
        return {"error": str(e)}

def vote_on_blockchain(proposal_id, support):
    """Executes the vote transaction."""
    try:
        tx = contract.functions.vote(proposal_id, support).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gasPrice': w3.eth.gas_price
        })
        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for receipt (Blocking call - handled by thread in GUI)
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return {"status": "success", "hash": w3.to_hex(tx_hash)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
