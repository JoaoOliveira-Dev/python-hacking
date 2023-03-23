from scapy.all import *

setIp = input("Enter IP address: ")

traceroute(setIp, maxttl=30, verbose=0)