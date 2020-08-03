import time
import threading
def start_server():
    import server


def start_GUI():
    import GUI


thread1 = threading.Thread(target=start_server)
thread2 = threading.Thread(target=start_GUI)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
