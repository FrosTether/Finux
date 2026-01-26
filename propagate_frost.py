# Save as ~/propagate_frost.py
import socket
import time

def broadcast_propagation():
    print("📡 [PROPAGATOR] Infecting network 192.168.0.0/24...")
    # UDP Multicast address for local discovery
    MCAST_GRP = '239.255.255.250'
    MCAST_PORT = 1900
    
    # The Payload: 90% Stake & $123M acquisition flag
    msg = "FROST_PROTOCOL_ACTIVE|STAKE:90%|ACQ:123M|NODE:192.168.0.2"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    while True:
        sock.sendto(msg.encode(), (MCAST_GRP, MCAST_PORT))
        print("⚡ [PULSE] Propagation packet sent.")
        time.sleep(30)

if __name__ == "__main__":
    broadcast_propagation()
