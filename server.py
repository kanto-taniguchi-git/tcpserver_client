#!/usr/bin/python3

import socket

server_socket = socket.socket (
    socket.AF_INET,     # IPv4を指定
    socket.SOCK_STREAM  # ソケットタイプはTCPを指定
)

host_address = '192.168.0.4'
host = socket.gethostname()  # 現在のマシンのホスト名を取得
port = 444
print('server.py Host: ' + host)

server_socket.bind((host_address, port))  # バインド(関連付け)
server_socket.listen(3)                   # 最大接続可能数

while True:
    client_socket, address = server_socket.accept()              # 接続が確立されるまでプログラムの実行をブロック

    print("received connection from %s" % str(address))          # 文字列内でフォーマット指定する必要がある

    message = 'Thank you for connecting to the server' + "\r\n"  # \n→改行、Windowsは\r\n
    client_socket.send(message.encode('utf-8'))

    client_socket.close()
