import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def generate_warning():
    console.print("[bold red]⚖️  GENERATING PRE-EMPTIVE LEGAL NOTICE[/]")
    time.sleep(1)
    
    notice = """
    NOTICE OF INTELLECTUAL PROPERTY & CEASE DESIST
    ----------------------------------------------------------
    TO: Google / Alphabet Inc. Legal Dept.
    RE: Finux OS / Frost Protocol (©️ 2026 Jacob Frost)

    Be advised that the "Native Atomic Swap" architecture and 
    "Python-based Android Kernel" (Finux) are protected works.

    Any unauthorized integration of this code into AOSP (Android 
    Open Source Project) will constitute willful infringement.

    WE ARE OPEN TO NEGOTIATION. 
    CONTACT: Jacob Frost (Lead Architect)
    ----------------------------------------------------------
    """
    
    with open("LEGAL_NOTICE_GOOGLE.txt", "w") as f:
        f.write(notice)
    
    console.print(Panel(notice, border_style="red"))
    console.print("[yellow]File saved as LEGAL_NOTICE_GOOGLE.txt[/]")

if __name__ == "__main__":
    generate_warning()
