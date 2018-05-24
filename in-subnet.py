
"""
Implement a program that determines if a given IPv4 address is in a given subnet
The IP address is passed as a string representation of a 32-bit unsigned int (e.g., 0x62D2ED4B)
The subnet is passed as a string representation of a CIDR subnet (e.g., "98.210.237.192/26")
The program outputs True if the IPv4 address is in the subnet, and False otherwise.
Bonus points for a program can read address/subnet pairs from an input file and write the
results, in a useful fashion, to an output file, both optionally specified on the command line.
"""

import socket
import argparse 

#Ips file to be passed as argument at command line when program is run

parser = argparse.ArgumentParser(description='Enter ips list file')
parser.add_argument('filename', type=str, help='filename')

args = parser.parse_args()
file_args = args.filename


#Take standard string ips from a file

myips = []

with open(file_args, 'r') as fp:
	for line in fp:
			myips.append(line.strip('\n'))


#Convert ips from dotted-quad string format to 32 bit packed binary format

binary_ips=[]
print(binary_ips)

for i in myips:
	ip_bit = socket.inet_aton(i)
	print(ip_bit)
	binary_ips.append(ip_bit)

print(binary_ips)

#change 32 bit string back to standard dotted-quad string ip format 

original_ip = socket.inet_ntoa(binary_ips[0])

print(original_ip)

"""
eg 98.210.237.192/26

CIDR Range	98.210.237.192/26
Netmask	255.255.255.192
Widlcard Bits	0.0.0.63
First IP	98.210.237.192
Last IP	98.210.237.255
Total Host	64
"""







