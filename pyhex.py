#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Esse arquivo precisa ser executado com o python3 e com o parâmetro da string, exemplo: python3 pyhex.py "string"

import os
import sys

try:
	string=sys.argv[1]
	cmd = "echo -n "+string+" | xxd -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
	os.system(cmd)
except IndexError:
	print("\nInforme a string!\n")
	
