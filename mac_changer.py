import subprocess
import optparse
import re as regex

def getting_arguments():
    obj = optparse.OptionParser()
    obj.add_option("-i","--interface",dest= "interface",help = "enter the -i --interface followed with interface to change new mac")
    obj.add_option("-m","--mac",dest= "new_mac",help = "Enter the -m --new_mac fallowed with macadresss")
    value,arguments = obj.parse_args()
    if not value.interface:
        obj.error("[+] Enter the interface to change mac address --help to take help is needed")
    elif not value.new_mac:
        obj.error("[+] Enter the  new mac Address")
    else:
        return value

def change(interface,mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def check(interface):
    ifconfig_str = subprocess.check_output(["ifconfig",interface])
    filtered_str = regex.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_str)
    if filtered_str:
        return  filtered_str
    else:
        print("[+] improper MAC adress not able to read")


#calling all functions in sequence

argument = getting_arguments()

change(interface = argument.interface,mac = argument.new_mac)

changed_mac = check(argument.interface)

if changed_mac[0] == argument.new_mac:
    print("[+] MAC address changed")
else:
    print("[-] MAC adress not changed")



