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




    ------------------2nd iteration
    def scan(ip):
        # Createing an arp_request object and Setting the value of pdst as the the ip range we have.
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                     # ff:ff:... is the broadcast mac address. This could be changed
    arp_request_broadcast = broadcast/arp_request                        # Scapy allows us to compbine packets with the forwardslash /
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)   # srp is a scapy function for send (s), receiving (r) custom parts (p). Returns 2 lists. Timeout == sec.
    print("----------------------Discovered----------------------")
    print("IP\t\t\tMAC Address\n")

    for element in answered:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)               # psrc == ip, hwsrc == MAC
        
    
           
 

scan("192.168.127.1/24")

'''

import scapy.all as scapy
import argparse # instead of optparse, which is deprecated but still will work in P2 and P3. 

def get_arguments():
    parserInstance = argparse.ArgumentParser()                                            # Create a parser object instance

    parserInstance.add_argument("-t", "--target", 
                        dest="target", 
                        help="Target IP / IP range.")
                            
    MyOptions = parserInstance.parse_args()

    if not MyOptions.target:
        parserInstance.error("[-] Please specify a target with -t <TARGET>, use --help for more info.")
    return MyOptions

def scan(ip):
    # Createing an arp_request object and Setting the value of pdst as the the ip range we have.
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                     # ff:ff:... is the broadcast mac address. This could be changed
    arp_request_broadcast = broadcast/arp_request                        # Scapy allows us to compbine packets with the forwardslash /
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)   # srp is a scapy function for send (s), receiving (r) custom parts (p). Returns 2 lists. Timeout == sec.
    
    clients_list = []

    for element in answered:
        client_dict = {"ip":element[1].psrc, "Mac": element[1].hwsrc }   # psrc == ip, hwsrc == MAC
        clients_list.append(client_dict)
    return clients_list

def print_Results(results_list):
    print("----------------------Discovered----------------------")
    print("IP\t\t\tMAC Address\n")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["Mac"])    
 
options = get_arguments()
scan_result = scan(options.target)
print_Results(scan_result)