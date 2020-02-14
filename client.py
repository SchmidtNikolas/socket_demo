import socket

s = socket.socket()
s.connect(('127.0.0.1',12345))
while True:
    send_data = input("Type here: \t")
    s.send(("\t"+send_data).encode());
    if(str == "Bye" or str == "bye"):
        break
    print("Server:\t",s.recv(1024).decode())
s.close()