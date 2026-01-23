from web3 import Web3
import json

# Configuration
RPC_URL = "YOUR_RPC_URL_HERE" # e.g., Base Mainnet or Testnet
CONTRACT_ADDRESS = "DEPLOYED_CONTRACT_ADDRESS"
PRIVATE_KEY = "YOUR_PRIVATE_KEY" # Secure this in a .env file later

web3 = Web3(Web3.HTTPProvider(RPC_URL))

# ABI Snippet (Simplified for voting)
contract_abi = '[{"inputs":[{"internalType":"uint256","name":"_proposalId","type":"uint256"},{"internalType":"bool","name":"_support","type":"bool"}],"name":"vote","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(contract_abi))

def cast_vote(proposal_id, support):
    print(f"Casting vote on Proposal {proposal_id}...")
    
    # Build Transaction
    account = web3.eth.account.from_key(PRIVATE_KEY)
    tx = contract.functions.vote(proposal_id, support).build_transaction({
        'from': account.address,
        'nonce': web3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': web3.to_wei('1', 'gwei')
    })
    
    # Sign & Send
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"Vote submitted! Hash: {web3.to_hex(tx_hash)}")

# Example Usage: Vote YES (True) on Proposal 1
# cast_vote(1, True)
