import threading,time

def worker():
    """thread worker function"""
    print('orker')
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()