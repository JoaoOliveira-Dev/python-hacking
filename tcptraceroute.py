#!/usr/bin/python3

from scapy.all import *

target = input("Informe um alvo: ")
port = int(input("Porta de destino: "))

ans,unans=sr(IP(dst=target,ttl=(1,30))/TCP(dport=port,flags="S"))
ans.summary(lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))
