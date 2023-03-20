from scapy.all import *

setIp = input("Enter IP address: ")
setPort = input("Enter Port: ")

# Create a TCP SYN packet
SYN = IP(dst=setIp)/TCP(dport=int(setPort), flags="S")