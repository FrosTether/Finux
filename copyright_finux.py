import os
import time
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- IP CONFIGURATION ---
OS_NAME = "Finux OS"
CODENAME = "FROID (Frozen Droid)"
OWNER = "Jacob Frost"
YEAR = "2026"
LICENSE_TYPE = "Proprietary / Closed Source (Core Kernel)"

def apply_copyright_stamp():
    console.print(f"[bold cyan]⚖️  APPLYING COPYRIGHT PROTECTION: {OS_NAME}[/]")
    time.sleep(1)
    
    # 1. Generate LICENSE File
    license_text = f"""
    FINUX OPERATING SYSTEM LICENSE AGREEMENT
    --------------------------------------------------
    COPYRIGHT ©️ {YEAR} {OWNER}. ALL RIGHTS RESERVED.
    
    This software ({OS_NAME} / {CODENAME}) is the intellectual property of 
    {OWNER}. Unauthorized copying, distribution, modification, or sale 
    of this software or its source code is strictly prohibited.
    
    The "Atomic Swap" and "Governance" modules are proprietary technologies.
    
    LICENSED TO:
    1. {OWNER} (Lead Architect)
    2. John Frost (Co-Founder / OG)
    --------------------------------------------------
    """
    
    with open("LICENSE", "w") as f:
        f.write(license_text)
    console.print("[green]✔ LICENSE file generated.[/]")

    # 2. Patch the Source Code Header
    target_files = ["finux_mobile.py", "boot_img.py"]
    
    for fname in target_files:
        if os.path.exists(fname):
            with open(fname, "r") as f:
                content = f.read()
            
            # Add/Update Header
            header = f"# {OS_NAME} ©️ {YEAR} {OWNER}\n"
            if header not in content:
                new_content = header + content
                with open(fname, "w") as f:
                    f.write(new_content)
                console.print(f"[green]✔ Copyright Header stamped on {fname}[/]")

def issue_certificate():
    print("")
    console.print(Panel(f"""
[bold yellow]CERTIFICATE OF REGISTRATION[/]
------------------------------------
[white]Work Title:[/white]     {OS_NAME}
[white]Author:[/white]         {OWNER}
[white]Year:[/white]           {YEAR}
[white]Status:[/white]         [bold green]COPYRIGHTED ©️[/]
[white]Build ID:[/white]       FROID_RC1_PROTECTED

[dim]This digital signature confirms that the codebase 
is the sole property of the Frost Protocol.[/dim]
    """, title="Intellectual Property Office (Simulated)", border_style="yellow"))

if __name__ == "__main__":
    apply_copyright_stamp()
    issue_certificate()
