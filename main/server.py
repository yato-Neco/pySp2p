import socket

host = "127.0.0.1"
port = 50007
buffa = 1024 # ネットワークのバッファサイズ

    #AFはIPv4
    #SOCK_STREAMはTCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #IPとport指定
    s.bind((host, port))
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
