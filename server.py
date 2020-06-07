import socket
import sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 1026))
s.listen(1)
conn, add = s.accept()
print(f'connection with {add} is established')
while True:
    # x = input("server ->")
    # conn.send(bytes(x, 'utf-8'))
    data = conn.recv(1024).decode()
    print(data)
