import socket

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print("Socket Up and running with a connection from",addr)
while True:
	rcvd_data = c.recv(1024).decode()
	print("Client:\t",rcvd_data)
	send_data = input("Type here: \t")
	c.send(("\t"+send_data).encode())
	if(send_data == "Bye" or send_data == "bye"):
		break
c.close()