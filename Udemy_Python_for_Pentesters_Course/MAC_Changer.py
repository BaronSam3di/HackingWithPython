#!/bin/bash/env python

'''MAC address control changer
The subprocess module will execute system commands regardless of the OS. IT will adapt to the OS.
see https://docs.python.org/3/library/subprocess.html
'''

# en0 MAC address ether = 38:f9:d3:83:27:4b

import subprocess
import optparse   
import re                                                                               # Module for taking in arguments when running the script

def get_arguments():
    parserInstance = optparse.OptionParser()                                            # Create a parser object instance

    parserInstance.add_option("-i", "--interface", 
                        dest="interface", 
                        help="New MAC address")
    parserInstance.add_option("-m", "--mac", 
                        dest="new_mac", 
                        help="Interface to change the MAC address")
                        
    (MyOptions, MyArguments) = parserInstance.parse_args()

    if not MyOptions.interface:
        parserInstance.error("[-] Please specify an interface with -i <INTERFACE>, use --help for more info.")
    elif not MyOptions.new_mac:
        parserInstance.error("[-] Please specify an new MAC with -m <MAC>, use --help for more info.")
    return MyOptions


def change_MAC(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])        
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_MAC(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))                  # check_output returns the output by the command given.
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) # Regex rules need to start with 'r'

    if mac_address_search_result:
        return mac_address_search_result.group(0)                                            # group(0) is the first result
    else:
        print("[-] Could not read MAC address.")

MyOptions = get_arguments()

current_mac = get_current_MAC(MyOptions.interface)
print("current_mac == " + str(current_mac))

# --- uncomment to implement changeing 
# change_MAC(MyOptions.interface, MyOptions.new_mac)

current_mac = get_current_MAC(MyOptions.interface)
if current_mac == MyOptions.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")


