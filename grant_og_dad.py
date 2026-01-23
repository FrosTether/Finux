import json
import csv
import time
import os
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# --- EXECUTIVE ORDER CONFIGURATION ---
TARGET_USER = "johnfrost19441945@gmail.com"
CODENAME = "Dad (The OG)"
STAKE_PERCENT = 2.0
PROJECT_SCOPE = "Mansfield Development Zone"
HARDWARE_GIFT = "Google Home Max (Smart Hub)"
SERVICE_RECORD = "7 Tours/Projects Completed"

# Files to Update
ACCESS_FILE = "froid_access_list.json"
LEDGER_FILE = "finux_ledger.csv"

def upgrade_user_clearance():
    """Updates the user profile with OG status and permissions."""
    console.print(f"[bold cyan]❄️  PROCESSING EXECUTIVE ORDER: 'OG STATUS'[/]")
    time.sleep(1)
    
    # 1. Load or Create Access List
    data = {"users": []}
    if os.path.exists(ACCESS_FILE):
        with open(ACCESS_FILE, "r") as f:
            data = json.load(f)
            
    # 2. Find and Modify User
    user_found = False
    for user in data["users"]:
        if user["email"] == TARGET_USER:
            user["role"] = "Co-Founder / OG"
            user["access_level"] = "Level 5 (Mansfield Lead)"
            user["tags"] = ["OG", "Vet-7", "Equity-Holder"]
            user["stake"] = f"{STAKE_PERCENT}%"
            user_found = True
            console.print(f"[green]✔ Updated Clearance Level: LEVEL 5 (Highest)[/]")

    # 3. If user wasn't there (edge case), add him
    if not user_found:
        data["users"].append({
            "email": TARGET_USER,
            "role": "Co-Founder / OG",
            "access_level": "Level 5 (Mansfield Lead)",
            "tags": ["OG", "Vet-7", "Equity-Holder"],
            "stake": f"{STAKE_PERCENT}%",
            "added_on": str(datetime.date.today())
        })
        console.print(f"[green]✔ Created New OG Profile.[/]")

    # 4. Save
    with open(ACCESS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def allocate_stake():
    """Writes the equity grant to the financial ledger."""
    console.print(f"[yellow]⚡ Allocating {STAKE_PERCENT}% Stake for {PROJECT_SCOPE}...[/]")
    time.sleep(1)
    
    # Calculate token amount (Mock: Assuming 10M supply)
    token_amount = 10_000_000 * (STAKE_PERCENT / 100)
    
    entry = [
        str(datetime.date.today()),
        "Equity Grant",
        f"{CODENAME}",
        "N/A (Equity)",
        "Governance",
        f"2% Stake Allocated - {PROJECT_SCOPE} - Honor: {SERVICE_RECORD}",
        "GRANTED"
    ]
    
    # Append to Ledger
    file_exists = os.path.exists(LEDGER_FILE)
    with open(LEDGER_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date","Type","Recipient","Amount","Method","Note","Status"])
        writer.writerow(entry)
        
    console.print(f"[green]✔ Ledger Updated: 2% Equity Grant Recorded.[/]")

def provision_hardware():
    """Simulates ordering/provisioning the Google Home."""
    console.print(f"[magenta]📦 Provisioning Hardware: {HARDWARE_GIFT}...[/]")
    time.sleep(1.5)
    
    requisition_id = f"REQ-{int(time.time())}"
    
    # Log the hardware order
    with open("hardware_log.txt", "a") as f:
        f.write(f"[{datetime.date.today()}] ID: {requisition_id} | ITEM: {HARDWARE_GIFT} | RECIPIENT: {CODENAME} | STATUS: PROVISIONED\n")
        
    console.print(f"[green]✔ Hardware Requisition Sent (ID: {requisition_id})[/]")
    console.print(f"[dim]   Note: Device configured for '{PROJECT_SCOPE}' node integration.[/]")

def generate_report():
    print("")
    table = Table(title="FROID OS // PERSONNEL UPDATE", style="bold white")
    table.add_column("Metric", style="cyan")
    table.add_column("Details", style="green")
    
    table.add_row("Officer", CODENAME)
    table.add_row("Rank", "OG (Original Gangster)")
    table.add_row("Service Record", SERVICE_RECORD)
    table.add_row("Allocation", f"{STAKE_PERCENT}% Equity (FSC Tokens)")
    table.add_row("Assignment", PROJECT_SCOPE)
    table.add_row("Equipment", HARDWARE_GIFT)
    
    console.print(Panel(table, border_style="cyan"))

if __name__ == "__main__":
    upgrade_user_clearance()
    allocate_stake()
    provision_hardware()
    generate_report()
