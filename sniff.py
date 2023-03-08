from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP):
        print(packet[TCP].payload)

sniff(filter="tcp", prn=packet_callback, store=0)
