import numpy as np
import sounddevice as sd # Requires: pip install sounddevice
import time

def generate_healing_tone(frequency, duration=60):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Simple Sine Wave Equation: y(t) = A * sin(2 * pi * f * t)
    tone = np.sin(2 * np.pi * frequency * t)
    
    print(f"🔊 BROADCASTING NEURO-TONE: {frequency}Hz")
    sd.play(tone, sample_rate)
    sd.wait()

if __name__ == "__main__":
    # Starting with 40Hz Gamma for cognitive clarity
    generate_healing_tone(40)
