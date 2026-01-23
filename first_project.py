import tarfile
import os
import time
import sys
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

# --- CONFIGURATION ---
BACKUP_NAME = "finux_backup.tar.gz"
RELEASE_NOTES_FILE = "RELEASE_NOTES.md"

# The text for the Release Notes we just drafted
RELEASE_NOTES_CONTENT = """
# RELEASE NOTES: Android 17 Release 1 (Finux Edition)
**Date:** January 23, 2026
**Codename:** Pumpkin Cheesecake
**Build ID:** AP3A.260123.001.FX1

## Executive Summary
This Release Candidate (RC1) merges the stable Android 16 AOSP framework 
with the experimental Finux Runtime Environment (Python-based Kernel).

## Key Features
1. **Finux Mobile Shell:** Terminal-based replacement for Pixel Launcher.
2. **Native Atomic Swap:** System-level crypto liquidation (ETH -> USDC).
3. **Governance:** Hardcoded 5% voting weight for Lead Developer.

## included Artifacts
- finux_mobile.py (Core OS)
- pay_larry_swap.py (Payment Module)
- ledger.py (Accounting)
- Android17_R1_GoogleSubmission.zip (Flashable Image)

## Sign-off
Jacob Frost
Lead Architect
"""

# List of files to include in the backup
PROJECT_FILES = [
    "finux_mobile.py",
    "pay_larry_swap.py",
    "ledger.py",
    "finux_ledger.csv",
    "governance_tool.py",
    "build_release_candidate.py",
    "Android17_R1_GoogleSubmission.zip",  # The package you just built
    "RELEASE_NOTES.md",
    "FUI.py",            # Desktop UI (Legacy)
    "bootloader.sh",     # Desktop Bootloader
    "setup_finux.py",    # Installer
    "deploy.py",         # Contract Deployer
    "contract_data.json" # Wallet Keys/Addresses
]

def create_archive():
    console.print(f"[bold white on blue] FINUX ARCHIVAL SYSTEM v1.0 [/]")
    print("")

    # 1. Write Release Notes to Disk
    with open(RELEASE_NOTES_FILE, "w") as f:
        f.write(RELEASE_NOTES_CONTENT)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:

        task = progress.add_task("[cyan]Scanning Project Files...", total=len(PROJECT_FILES) + 5)
        
        # 2. Create the Tarball
        with tarfile.open(BACKUP_NAME, "w:gz") as tar:
            for filename in PROJECT_FILES:
                if os.path.exists(filename):
                    time.sleep(0.1) # Simulate processing
                    tar.add(filename)
                    progress.console.log(f"   [green]✔ Archived:[/green] {filename}")
                else:
                    progress.console.log(f"   [dim yellow]⚠ Skipped (Missing):[/] {filename}")
                
                progress.update(task, advance=1)
            
            # Finalize
            progress.update(task, advance=5)

    # 3. Validation
    file_size = os.path.getsize(BACKUP_NAME) / 1024
    print("")
    console.print(f"[bold green]✅ BACKUP COMPLETE: {BACKUP_NAME}[/]")
    console.print(f"   Size: {file_size:.2f} KB")
    console.print(f"   Location: {os.getcwd()}/{BACKUP_NAME}")
    console.print("[dim]   Keep this file safe. It contains your OS, Wallet Keys, and Ledger.[/]")

if __name__ == "__main__":
    create_archive()
