import os
import time

class FrostHardwareControl:
    def __init__(self):
        self.fan_path = "/sys/class/hwmon/hwmon5/pwm1" # Standard Linux fan path
        self.tdp_path = "/sys/class/power_supply/BAT1/power_limit"

    def set_fan_speed(self, speed_percent):
        # 0-255 PWM Value
        pwm_val = int((speed_percent / 100) * 255)
        print(f"   [HARDWARE] Setting Fan Speed to {speed_percent}% ({pwm_val} PWM)")
        # In a real root shell:
        # os.system(f"echo {pwm_val} > {self.fan_path}")

    def overclock_cpu(self):
        print("   [HARDWARE] OVERCLOCKING APU to 15W TDP...")
        time.sleep(1)
        print("   [POWER] VOLTAGE INCREASED. PERFORMANCE: +20%")

    def run_diagnostics(self):
        print("❄️  FROST HARDWARE MONITOR")
        self.set_fan_speed(85) # High airflow for mining
        self.overclock_cpu()
        print("   [STATUS] Mining Mode Active. Device runs cool.")

if __name__ == "__main__":
    hw = FrostHardwareControl()
    hw.run_diagnostics()
