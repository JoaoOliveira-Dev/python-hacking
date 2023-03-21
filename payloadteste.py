from scapy.all import *

setIp = input("Enter IP address: ")
ip = IP(dst=setIp)

setPort = input("Enter Port: ")
port = int(setPort)

tcp = TCP(dport=port)/Raw(load="Hello World")

pkt = ip/tcp

sr(pkt)