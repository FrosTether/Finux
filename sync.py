import socket
import json
import os
from rich.console import Console

console = Console()

# --- Network Configuration ---
BUFFER_SIZE = 4096  # Standard size for data packets
SYNC_PORT = 8888    # Dedicated port for Frost Protocol sync

def start_node_server():
    """Listens for incoming sync requests from other peers."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', SYNC_PORT))  # Bind to all interfaces
        s.listen(5)
        console.print(f"[bold green]Node Server Active. Listening on port {SYNC_PORT}...[/bold green]")
        
        while True:
            conn, addr = s.accept()
            with conn:
                console.print(f"📡 Sync request from: {addr}")
                # Load the local ledger to send to the peer
                if os.path.exists('frost_chain.json'):
                    with open('frost_chain.json', 'rb') as f:
                        data = f.read()
                        conn.sendall(data)  # Send the entire chain
                console.print("✅ Ledger data transmitted.")

def request_sync(peer_ip):
    """Connects to a peer to download their version of the chain."""
    console.print(f"[bold cyan]Attempting to sync with peer: {peer_ip}...[/bold cyan]")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((peer_ip, SYNC_PORT))  # Establish handshake
            data = b""
            while True:
                packet = s.recv(BUFFER_SIZE)  # Receive data in chunks
                if not packet:
                    break
                data += packet
            
            # Save the new ledger locally
            with open('frost_chain.json', 'wb') as f:
                f.write(data)
            console.print("[bold green]Success! Local ledger updated to peer version.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Sync Failed: {e}[/bold red]")

if __name__ == "__main__":
    # In a real scenario, you'd run the server in a thread
    mode = console.input("Run as [S]erver or [C]lient? ").upper()
    if mode == 'S':
        start_node_server()
    elif mode == 'C':
        target = console.input("Enter Peer IP: ")
        request_sync(target)
