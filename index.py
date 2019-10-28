

import ipaddress
import socket

path = ''

firstint = 16843009 #ip->1.1.1.1
lastint = 4294967295 #ip->255.255.255.255

f = open(path,'a')

for i in range(firstint,lastint+1):
	try:
		addr = ipaddress.IPv4Address(i)
		print(addr)
		net = socket.gethostbyaddr(str(addr))
		print(net)
		f.write("{}=>{}".format(i,net))
		del addr,net
	except SyntaxError:
		continue
	except socket.herror:
		continue
f.close()


