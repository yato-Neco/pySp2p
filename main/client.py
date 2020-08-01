import socket

host = "127.0.0.1"
port = 50007
buffa = 1024 # ネットワークのバッファサイズ

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #サーバ指定
    s.connect((host, port))
    #サーバーにメッセージ送信
    s.sendall(b"hello")

    data = s.recv(buffa)

    print(repr(data))
