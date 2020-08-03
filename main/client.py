import socket

def client(msg, setting):
    host2 = str(msg)
    port1 = 80
    buffa = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         # ネットワークのバッファサイズ
            #サーバ指定
        s.connect((host2, port1))
            #サーバーにメッセージ送信
        s.sendall(setting.encode('unicode-escape'))

        data = s.recv(buffa)
        print(repr(data.decode('unicode-escape')))
