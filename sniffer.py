from scapy.all import *
def packet_callback(packet):
    print(packet.summary())
print("Capturing 10 packets...")
sniff(prn=packet_callback, count=10)
