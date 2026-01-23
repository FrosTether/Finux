from web3 import Web3
from ecdsa import VerifyingKey, SECP256k1
import binascii

# Connect to a blockchain node (e.g., Infura, Alchemy, or a local node)
w3 = Web3(Web3.HTTPProvider('https://polygon-mainnet.infura.io/v3/YOUR_PROJECT_ID'))

def process_authorized_transaction(public_key_hex, signature_hex, challenge, tx_data):
    """
    Verifies the biometric signature and broadcasts the transaction.
    """
    try:
        # 1. Verify the biometric-authorized signature
        vk = VerifyingKey.from_string(binascii.unhexlify(public_key_hex), curve=SECP256k1)
        is_valid = vk.verify(binascii.unhexlify(signature_hex), challenge.encode())
        
        if not is_valid:
            return {"status": "error", "message": "Invalid biometric signature"}

        # 2. Build the transaction payload
        # The 'nonce' here is the account's transaction count on the blockchain
        tx = {
            'nonce': w3.eth.get_transaction_count(tx_data['from']),
            'to': tx_data['to'],
            'value': w3.to_wei(tx_data['amount'], 'ether'),
            'gas': 21000,
            'maxFeePerGas': w3.to_wei('50', 'gwei'),
            'maxPriorityFeePerGas': w3.to_wei('2', 'gwei'),
            'chainId': 137 # Polygon Mainnet
        }

        # 3. Broadcast the signed transaction
        # Note: The backend typically signs with its own hot wallet for gas fees 
        # or forwards the raw transaction signed by the mobile app hardware.
        tx_hash = w3.eth.send_raw_transaction(tx_data['signed_raw_tx'])
        
        return {"status": "success", "tx_hash": tx_hash.hex()}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
