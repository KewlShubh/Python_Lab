import socket
import sys
import time
x=socket.socket()
h_name= input(str(" Enter the hostname of the server"))
port = 2200

x.connect((h_name,port))
print("Connected to chat server")

while 1: 
   incoming_message=x.recv(1024)
   incoming_message=incoming_message.decode()
   print(" Server :", incoming_message)
   message= input(str(">>"))
   message =message.encode()
   x.send(message)
   print(" message has been sent...")