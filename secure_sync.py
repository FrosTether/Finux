import socket
import json
import os
from rich.console import Console
from validator import is_chain_valid  # Import your existing validation logic

console = Console()
SYNC_PORT = 8888
BUFFER_SIZE = 4096

def receive_and_validate(peer_ip):
    """Requests, validates, and saves a peer's ledger."""
    console.print(f"[bold cyan]Initiating secure sync with {peer_ip}...[/bold cyan]")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((peer_ip, SYNC_PORT))
            raw_data = b""
            while True:
                packet = s.recv(BUFFER_SIZE)
                if not packet: break
                raw_data += packet
            
            # 1. Parse incoming JSON
            incoming_ledger = json.loads(raw_data.decode())
            
            # 2. Immediate Integrity Check
            console.print("🔍 Auditing incoming ledger integrity...")
            if is_chain_valid(incoming_ledger):
                # 3. Save only if verified
                with open('frost_chain.json', 'w') as f:
                    json.dump(incoming_ledger, f, indent=4)
                console.print("[bold green]✅ Sync Complete: Peer ledger verified and saved.[/bold green]")
            else:
                console.print("[bold red]❌ Sync Aborted: Peer sent a corrupted or tampered ledger![/bold red]")
                
        except Exception as e:
            console.print(f"[bold red]Sync Error: {e}[/bold red]")

if __name__ == "__main__":
    target = console.input("Enter Peer IP for Secure Sync: ")
    receive_and_validate(target)
