# Frost Protocol: Light-Pulse Transmitter (LICO Tier)
import time
from hardware import LED

def transmit_light_code(message):
    binary_stream = ''.join(format(ord(i), '08b') for i in message)
    # The 'Amiahdo' Preamble (Sync pulse)
    LED.on(); time.sleep(0.1); LED.off(); time.sleep(0.1) 
    
    for bit in binary_stream:
        if bit == '1':
            LED.on() # 888Hz Pulse overlay
        else:
            LED.off()
        time.sleep(0.001) # Ultra-fast switching
    LED.off()
