# PRODIGY_CS_05.PY
TASK-05
Develop a packet sniffer tool  that captures and  analyzes network packets. Display relevant information  such as source and destination ip addresses, protocols and payload data . Ensure that ethical use of the tool for educational purposes.

Network Packet Analyzer:

A network packet analyzer, also known as a packet sniffer, is a tool that captures and analyzes network traffic. It inspects data packets as they are transmitted over a network, allowing users to view information such as source and destination IP addresses, protocols, and payload data.

Common Uses of a Network Packet Analyzer:

1. Network troubleshooting: Helps to identify network performance issues or misconfigurations.

2. Security monitoring: Detects suspicious network activity, like unauthorized access or malware communication.

3. Protocol analysis: Examines how different network protocols (e.g., TCP, UDP, ICMP) behave on a network.

4. Educational purposes: Helps students and network engineers understand networking fundamentals.

HOW IT WORKS:
Packet Capture with Scapy: The sniff() function from scapy is used to capture packets. It takes prn=packet_callback as a parameter, which means that for every captured packet, the packet_callback function will be called. IP Layer Analysis: The tool checks if the packet contains an IP layer, and if so, extracts and prints the source and destination IP addresses and the protocol number. TCP/UDP/ICMP Protocol Analysis: Depending on the protocol (TCP, UDP, ICMP), it further extracts and prints information such as port numbers for TCP and UDP, or the type and code for ICMP. Payload Display: The tool also prints the raw payload data in the packet, which can be useful for further analysis.
Repository Contents:
PRODIGY_CS_05.py : The main Python script containing the implementation of the Network Packet Analyzer. README.md : This file, providing an overview of the task and the project
