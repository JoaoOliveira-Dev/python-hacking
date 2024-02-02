#!/usr/bin/python3

from scapy.all import *

dest = input("\nDestination: ")
port = int(input("Destination port: "))
flag = input("Flags: ")

ip = IP(dst=dest)
tcp = TCP(dport=port, flags=flag)

pkt = ip/tcp

srloop(pkt, count=1)