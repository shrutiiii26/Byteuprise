from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        if proto == 6:  # TCP
            if TCP in packet:
                tcp_sport = packet[TCP].sport
                tcp_dport = packet[TCP].dport
                print(f"TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")

        elif proto == 17:  # UDP
            if UDP in packet:
                udp_sport = packet[UDP].sport
                udp_dport = packet[UDP].dport
                print(f"UDP Packet: {ip_src}:{udp_sport} -> {ip_dst}:{udp_dport}")

        elif proto == 1:  # ICMP
            if ICMP in packet:
                icmp_type = packet[ICMP].type
                print(f"ICMP Packet: {ip_src} -> {ip_dst} (Type: {icmp_type})")

def main():
    # Capture packets on the default interface
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
