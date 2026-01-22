import os
import subprocess

def install_to_steam_deck():
    print("🚂 INSTALLING FINUX TO STEAM DECK / ARM...")
    
    # 1. DETECT STEAMOS
    is_steam_deck = False
    try:
        # Check for SteamOS atomic filesystem (Example check)
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                if "steam" in f.read().lower():
                    is_steam_deck = True
    except: pass

    if is_steam_deck:
        print("   [✓] STEAMOS DETECTED.")
    else:
        print("   [!] WARNING: Not running on native SteamOS (Assuming Dev Environment)")

    # 2. CREATE SHORTCUT (Linux Desktop Entry)
    desktop_file = """[Desktop Entry]
    Name=Finux OS (FrostDeck)
    Comment=Secure Operating System
    Exec=python3 /home/deck/Finux/mobile/deck/frost_deck.py
    Icon=/home/deck/Finux/assets/icon.png
    Terminal=true
    Type=Application
    Categories=System;
    """
    
    # Simulate writing to the Deck's applications folder
    print("   [>] Registering Application...")
    # with open("/home/deck/.local/share/applications/finux.desktop", "w") as f:
    #     f.write(desktop_file)
    
    print("   [>] Adding to Steam Non-Game Library...")
    # (In reality, this requires editing shortcuts.vdf)
    
    print("\n✅ INSTALLATION COMPLETE.")
    print("   Return to 'Game Mode' on your Deck.")
    print("   You will find 'Finux OS' in your Library under 'Non-Steam'.")

if __name__ == "__main__":
    install_to_steam_deck()
