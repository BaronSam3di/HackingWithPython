'''
Broadcast MAC address sends the packet to all clients on the network to find the ip address of a particular device.
Only the one with the ip address will respond.

https://scapy.readthedocs.io/en/latest/
https://scapy.readthedocs.io/en/latest/usage.html?highlight=arp-ping#arp-ping

    scapy.arping(ip)    # arping is a built in arp scanner function of scapy   

import scapy.all as scapy

def scan(ip):
    # Createing an arp_request object and Setting the value of pdst as the the ip range we have.
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()

    # This will list all the felids available to set on the "scapy.ARP" object with; Felid, Desc, Default 
    scapy.ls(scapy.ARP())
    print(arp_request.summary())

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")            # ff:ff:... is the broadcast mac address
    print(broadcast.summary())
    broadcast.show()

    arp_request_broadcast = broadcast/arp_request               # Scapy allows us to compbine packets with the forwardslash /
    print(arp_request_broadcast.summary())
    
    arp_request_broadcast.show()

'''

import scapy.all as scapy

def scan(ip):
    # Createing an arp_request object and Setting the value of pdst as the the ip range we have.
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                     # ff:ff:... is the broadcast mac address. This could be changed
    arp_request_broadcast = broadcast/arp_request                        # Scapy allows us to compbine packets with the forwardslash /
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)   # srp is a scapy function for send (s), receiving (r) custom parts (p). Returns 2 lists. Timeout == sec.
    print("----------------------Discovered----------------------")
    print("IP\t\t\tMAC Address\n")

    for element in answered:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)  # psrc == ip, hwsrc == MAC
        
    
           
 

scan("192.168.127.1/24")