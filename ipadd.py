#!/usr/bin/python
# Showing the en0 ip address/mask/MAC in preatty table
# Add Default Gateway info

from prettytable import PrettyTable
import commands

# Converts the hex network address mask in int mask

def hex2int(hex):
    result = ''
    hex = hex[2:]
    for x in range(4):
        duma = '0x' + hex[x * 2:x * 2 + 2]
        result += str(int(duma, 0)) + '.'
    return result[0:15]


output = commands.getstatusoutput('ifconfig en0 | grep netmask')
output_mac = commands.getstatusoutput('ifconfig en0 | grep ether ')

output = output[1].split()
output_mac = output_mac[1].split()

output[3] = hex2int(str(output[3]))

x = PrettyTable(["Interface", "IP Address", "Mask", "MAC Adress"])
x.align["IP Address"] = "c"
x.padding_width = 1
x.add_row(["en0", output[1], output[3], output_mac[1]])

print
print x
print
