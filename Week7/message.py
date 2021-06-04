import sys
import socket
import time
x=socket.socket()
h_name= socket.gethostname()
print("server will start on host: ", h_name)
port= 8080
x.bind((h_name, port))
print("Server done binding to host and port succesfully")
print("server is waiting for incoming connections")
x.listen(1)
connection,address= x.accept()
print(address, " Has connected to the server and is now online...")



