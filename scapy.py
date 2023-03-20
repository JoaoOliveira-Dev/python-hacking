from scapy.all import *

setIp = input("Enter IP address: ")
ip = IP(dst=setIp)

setPort = input("Enter Port: ")
port = int(setPort)

tcp = TCP(dport=port, flags="S")

pkt = ip/tcp

sr(pkt)