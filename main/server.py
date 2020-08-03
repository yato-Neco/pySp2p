import socket

def server():
    host = socket.gethostname()
    print(host)
    ip = socket.gethostbyname(host)
    print(ip)
    #AFはIPv4
    #SOCK_STREAMはTCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host2 = ip
        port2 = 80
        buffa = 1024 # ネットワークのバッファサイズ
        #IPとport指定
        s.bind((host2, port2))
        #接続
        s.listen(1)
        #接続待機
        while True:
            # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
            conn, addr = s.accept()
            with conn:
                while True:
                    #データ受け取り
                    data = conn.recv(buffa)
                    if not data:
                        break
                    print("data : {}, addr {}".format(data.decode('unicode-escape'), addr))
                        #クライアントにデータを返す
                    conn.sendall(b"server: " + data)
server()
