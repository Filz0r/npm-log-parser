#!/usr/bin/env python3
import re
import os

path = os.path.realpath(__file__)
main_path = os.path.realpath(__file__)[:len(path) - 13]
log_path = main_path + 'logs/default.log'
pattern = 'GET http localhost-nginx-proxy-manager'

public_ip = input('what is your public IP? ')
print(public_ip)

ct = 0
hand = open(log_path, 'rt')
test = open(main_path + 'parsed/parsed-default.log', 'w+')

for line in hand:
    line = line.rstrip()
    stuff = re.findall(pattern, line)
    if line.find(pattern) != -1 and line.find(public_ip) == -1:
        test.write(str(line + '\n'))
        ct = ct + 1
    if len(stuff) != 1 : continue

print('done, found ' + str(ct) + ' results')



