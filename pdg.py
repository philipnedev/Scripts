#!/usr/bin/python
# Find and start ping-ing the Default Gateway

from prettytable import PrettyTable
import commands
from subprocess import call


#Get the default gateway IP address
dg_output = commands.getstatusoutput('netstat -rn | grep en0 | grep default | grep -v fe80')
dgip = dg_output[1].split()[1] #gets the line from the output, splits it and get the 1-element(the IP address)

#Start pinging the ip address
call(["ping", dgip])



