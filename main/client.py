import socket
import os
import sys

def main(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = "127.0.0.1"
        port = 50007
        buffa = 1024 # ネットワークのバッファサイズ
            #サーバ指定
        s.connect((host, port))
            #サーバーにメッセージ送信
        s.sendall(msg.encode('unicode-escape'))

        data = s.recv(buffa)
        print(repr(data.decode('unicode-escape')))
