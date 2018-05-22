
#Convert a string ip address into a single integer value

myip='129.121.177.10'

#split the ip address down into octets
a,b,c,d=myip.split('.')

octets = [a,b,c,d]

#convert octet strings to ints
octets = [int(i) for i in octets]

ip_integers = []


ip_integers.append(octets[0]*256**3)
ip_integers.append(octets[1]*256**2)
ip_integers.append(octets[2]*256)
ip_integers.append(octets[3])

final_int = sum(ip_integers)

print(final_int)

#Convert ip to 32 bit packed binary format

import socket

socket.inet_aton(myip)





