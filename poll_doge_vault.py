DOGE_VAULT_ADDR = "DJTDVRxJGtcuSsxwT7GHbkdCabqaTa1C7s"
DOGE_API_URL = f"https://sochain.com/api/v2/get_tx_received/DOGE/{DOGE_VAULT_ADDR}"
# Linked identities: Your Doge sending addresses → your Base wallet
LINKED_IDENTITIES = {
    # Replace with your actual Dogecoin address that sends to the tunnel
    # Example format: 'DABC123def456...' : 'DJTDVRxJGtcuSsxwT7GHbkdCabqaTa1C7s'
    'YOUR_DOGE_SENDING_ADDRESS_HERE': '0xba2ae424d960c26247dd6c32edc70b295c744c43',
    
    # Add backups or secondary wallets if you have them
    # 'DAnotherWalletYouUse...': '0x6556fBB94508bFa8CE919f691ef71d4181D36D20',
}