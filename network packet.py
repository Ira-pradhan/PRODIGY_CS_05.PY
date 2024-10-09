pip install scapy

from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"\n[+] New Packet: {ip_src} -> {ip_dst} (Protocol: {protocol})")
        
        # If the packet has a TCP layer
        if TCP in packet:
            print(f"[TCP] Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}")
        
        # If the packet has a UDP layer
        elif UDP in packet:
            print(f"[UDP] Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}")
        
        # If the packet has an ICMP layer
        elif ICMP in packet:
            print(f"[ICMP] Type: {packet[ICMP].type} Code: {packet[ICMP].code}")
        
        # Print the raw payload
        print(f"Payload: {bytes(packet[IP].payload)}")

def main():
    print("Starting Packet Sniffer...")
    # Sniff packets on the network
    sniff(prn=packet_callback, store=0)

if _name_ == "_main_":
    main()