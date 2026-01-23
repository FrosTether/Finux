import time
import sys
import json
import os
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel

console = Console()

# --- CONFIGURATION ---
NEW_OS_NAME = "FROID OS v1.0 (Frozen Droid)"
BUILD_ID = "FROID_RELEASE_1_2026"
CENTINET_NODE_IP = "192.168.1.105 (CENTINET_HUB)" # Simulation
NEW_USER = "johnfrost19441945@gmail.com"

# --- SYSTEM FILES TO PATCH ---
SYSTEM_FILES = ["finux_mobile.py", "boot_img.py", "finux_ledger.csv"]

def clear_screen():
    os.system('clear')

def patch_system_identity():
    """Renames internal system strings from Finux/Android 17 to FROID."""
    console.print(f"[bold cyan]❄️  INITIATING FROID REBRANDING PROTOCOL...[/]")
    time.sleep(1)
    
    # 1. Update Bootloader Identity
    if os.path.exists("boot_img.py"):
        with open("boot_img.py", "r") as f:
            content = f.read()
        
        new_content = content.replace("Android 17 Pumpkin Cheesecake", NEW_OS_NAME)
        new_content = new_content.replace("Finux", "FROID")
        
        with open("boot_img.py", "w") as f:
            f.write(new_content)
        console.print("[green]✔ Bootloader patched to FROID Kernel.[/]")

    # 2. Update Mobile Shell Identity
    if os.path.exists("finux_mobile.py"):
        with open("finux_mobile.py", "r") as f:
            content = f.read()
        
        # Replace Header Text
        if "ANDROID 17" in content:
            content = content.replace("ANDROID 17 (PUMPKIN CHEESECAKE)", NEW_OS_NAME)
        elif "FINUX MOBILE" in content:
            content = content.replace("FINUX MOBILE", "FROID OS")
            
        with open("finux_mobile.py", "w") as f:
            f.write(content)
        console.print("[green]✔ Shell Interface updated to FROID UI.[/]")

def push_ota_update():
    """Simulates pushing data to Phone and Centinet."""
    print("")
    console.print(f"[bold white on blue] 📡 FROID OTA DISTRIBUTION NETWORK [/]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        
        # Task 1: Local Phone Update
        task1 = progress.add_task("[yellow]Flashing Local Device (Phone)...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(task1, advance=5)
        progress.console.log("[green]✔ Local System Updated: FROID v1.0 Active[/]")

        # Task 2: Centinet Update
        task2 = progress.add_task(f"[magenta]Pushing to CENTINET ({CENTINET_NODE_IP})...", total=100)
        for _ in range(25):
            time.sleep(0.08) # Slower because "network"
            progress.update(task2, advance=4)
        progress.console.log("[green]✔ Centinet Node Synced: FROID Protocol Installed[/]")

def onboard_user():
    """Adds Dad to the permission system."""
    print("")
    console.print(f"[bold green]👤 PROVISIONING NEW USER[/]")
    time.sleep(1)
    
    # Create/Update Access Control List
    acl_file = "froid_access_list.json"
    data = {"users": []}
    
    if os.path.exists(acl_file):
        with open(acl_file, "r") as f:
            data = json.load(f)
    
    # Check if user exists
    existing_emails = [u["email"] for u in data["users"]]
    if NEW_USER not in existing_emails:
        new_entry = {
            "email": NEW_USER,
            "role": "Senior Observer",
            "access_level": "Level 2 (Read/Audit)",
            "added_on": time.strftime("%Y-%m-%d")
        }
        data["users"].append(new_entry)
        
        with open(acl_file, "w") as f:
            json.dump(data, f, indent=4)
        
        console.print(f"[green]✔ Added {NEW_USER} to Governance Layer.[/]")
        console.print(f"   Role: Senior Observer")
        console.print(f"   Permissions: View Ledger, Monitor Centinet")
    else:
        console.print(f"[yellow]⚠ User {NEW_USER} is already authorized.[/]")

def main():
    clear_screen()
    console.print(Panel.fit("[bold cyan]❄️  PROJECT FROID INSTALLER ❄️[/]", border_style="cyan"))
    
    patch_system_identity()
    push_ota_update()
    onboard_user()
    
    print("")
    console.print(Panel(f"""
[bold green]UPDATE SUCCESSFUL[/]
------------------
[white]System Name:[/] {NEW_OS_NAME}
[white]Build ID:[/]    {BUILD_ID}
[white]Nodes:[/]       2 (Phone + Centinet)
[white]Team:[/]        Jacob Frost (Lead), John Frost (Observer)
    """, title="System Status", border_style="green"))
    
    console.print("[dim]Rebooting into FROID...[/]")
    time.sleep(3)
    os.system("python finux_mobile.py") # Relaunches the UI (now rebranded)

if __name__ == "__main__":
    main()
