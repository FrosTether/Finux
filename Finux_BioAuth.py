import time
import os
from collections import deque

class FinuxBioAuth:
    def __init__(self):
        self.device_id = None
        # Rolling buffer to store timestamps of 'Blink' signals
        self.blink_timestamps = deque(maxlen=3) 
        # App to launch (FrostMines)
        self.target_package = "com.frostprotocol.mines"
        print("[*] Finux Bio-Auth Service: STARTED")
        print("[*] Security Level: HIGH (GrapheneOS Vault)")

    def launch_secure_app(self):
        """
        Triggers the app launch via ADB when authentication passes.
        """
        print(f"\n[!!!] MENTAL PASSKEY ACCEPTED [!!!]")
        print(f"[*] Decrypting Vault...")
        print(f"[*] Launching: {self.target_package}")
        
        # ADB command to launch the app (using 'monkey' is a reliable shortcut)
        cmd = f"adb shell monkey -p {self.target_package} -c android.intent.category.LAUNCHER 1"
        os.system(cmd)
        
        # Clear buffer to prevent double-triggering
        self.blink_timestamps.clear()

    def process_signal(self, signal_type):
        """
        Analyzes incoming signals for the specific 'Triple Blink' pattern.
        Logic: 3 Blinks detected within a 2-second window.
        """
        current_time = time.time()

        if signal_type == "BLINK":
            print(f"    > Blink detected at {current_time:.2f}")
            self.blink_timestamps.append(current_time)

            # Check if we have 3 blinks recorded
            if len(self.blink_timestamps) == 3:
                first_blink = self.blink_timestamps[0]
                last_blink = self.blink_timestamps[-1]

                # If the time difference between the 1st and 3rd blink is < 2.0 seconds
                if (last_blink - first_blink) < 2.0:
                    self.launch_secure_app()
                else:
                    # Optional: Print debug info if too slow
                    # print("    [!] Sequence too slow. Resetting.")
                    pass
        else:
            # Handle other noise or signals (e.g., 'FOCUS', 'RELAX')
            print(f"    . Neural Noise: {signal_type}")

    def simulate_neural_stream(self):
        """
        Simulates a real-time stream of brain activity.
        """
        print("[*] Listening to N1 Stream... (Waiting for Triple Blink)")
        
        # A sequence representing: Noise -> Noise -> TRIPLE BLINK -> Noise
        simulation_sequence = [
            "ALPHA_WAVE", "BETA_WAVE",  # Background noise
            "BLINK",                    # 1st Blink
            "ALPHA_WAVE",               # Slight noise between blinks is normal
            "BLINK",                    # 2nd Blink
            "BLINK",                    # 3rd Blink (Trigger!)
            "BETA_WAVE", "ALPHA_WAVE"   # Back to normal
        ]

        for signal in simulation_sequence:
            time.sleep(0.4) # Simulate time gap between signals
            self.process_signal(signal)

if __name__ == "__main__":
    # Ensure ADB is connected
    # os.system("adb connect 192.168.x.x") # Uncomment for wireless ADB
    
    auth_system = FinuxBioAuth()
    auth_system.simulate_neural_stream()
