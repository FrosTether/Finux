"""
FROSTOISE: The Frost Protocol Search & Uplink Engine
Target: 1655 West Main Node, Bellevue
Owner: voluntaryistj@gmail.com
Status: 100% Pressure (♍🧲 x1337)
"""

import os
import sys

# --- PRE-FLIGHT ENVIRONMENT FIXES ---
# Fixes the 'CRITICAL' clipboard crash in Termux (Log 5144.png)
os.environ['KIVY_CLIPBOARD'] = 'dummy'

try:
    from kivy.app import App
    from kivy.uix.textinput import TextInput
    from kivy.clock import Clock
    from kivy.core.window import Window
    from kivy.core.audio import SoundLoader
except ImportError:
    print("❌ [ERROR] Kivy not found. Run: pip install kivy")
    sys.exit(1)

# --- CORE LOGIC ---

class FrostSearch(TextInput):
    """
    Advanced Search Bar with Debouncing to prevent AI Flooding.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debounce = None
        self.hint_text = "Search Frost Protocol..."
        self.multiline = False
        self.background_color = (0.1, 0.1, 0.1, 1)  # Dark Mode
        self.foreground_color = (0, 0.7, 1, 1)      # Frost Blue

    def on_text(self, instance, value):
        if self.debounce:
            self.debounce.cancel()
        # Set search delay to 0.6 seconds after typing stops
        self.debounce = Clock.schedule_once(lambda dt: self.uplink(value), 0.6)

    def uplink(self, query):
        if query.strip():
            print(f"📡 [UPLINK] AI Target Acquired: {query}")
            # Placeholder for Frequency Generator or FFmpeg processing
            # os.system(f"echo 'Query: {query}' | mail -s 'Search Trigger' voluntaryistj@gmail.com")

class FrostoiseApp(App):
    def build(self):
        self.title = "Frostoise v1.3.37"
        
        # --- INITIALIZATION LOG ---
        print("\033[94m")
        print("  _____               _       _ ")
        print(" |  ___| __ ___  ___ | |_ ___| |")
        print(" | |_ | '__/ _ \/ __|| __/ __| |")
        print(" |  _|| | | (_) \__ \| |_\__ \_|")
        print(" |_|  |_|  \___/|___/ \__|___(_)")
        print("\n[SYSTEM] HYDRO PUMP AT 100% PRESSURE")
        print("[NODE] Monroeville Batch Cycle Active")
        print("\033[0m")

        # --- AUTO-MAIL TRIGGER ---
        # Dispatches status update to the primary voluntaryist uplink
        mail_cmd = (
            "echo 'Frostoise Core Online. Node 1655 W Main: INITIATED.' | "
            "mail -s '♍🧲 x1337 Status' voluntaryistj@gmail.com"
        )
        os.system(mail_cmd)

        return FrostSearch()

if __name__ == "__main__":
    # Ensure Pulseaudio is primed before launch
    os.system("pulseaudio --start --exit-idle-time=-1")
    FrostoiseApp().run()
