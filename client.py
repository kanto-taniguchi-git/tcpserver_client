#!/usr/bin/python3

import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host_address = '192.168.0.4'
host = socket.gethostname()
port = 444
print('client.py Host: ' + host)

client_socket.connect((host_address, port))  # 指定されたIPアドレスとポート番号を持つサーバーに接続

message = client_socket.recv(1024)           # 最大1024バイト

client_socket.close()

print(message.decode('utf-8'))