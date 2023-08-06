from threading import Lock, Thread
from time import sleep

# def run(content, delay=1):
#     sleep(delay)
#     print(content)

# thread1 = threading.Thread(target=run, args=("run 1", 1))
# thread2 = threading.Thread(target=run, args=("run 2", 1))

# thread1.start()
# thread2.start()
# print(threading.active_count())
# thread1.join()
# thread2.join()
# print("main therad")



#######################

# def t1(lock):
#     lock.acquire()
#     sleep(1)
#     print("t1")
#     lock.release()

# def t2(lock):
#     lock.acquire()
#     sleep(1)
#     print("t2")
#     lock.release()

# lock = Lock()
# thread1 = Thread(target=t1, args=(lock,))
# thread2 = Thread(target=t2, args=(lock,))

# thread1.start()
# thread2.start()




#######################


# def print_values(values, start_lock, end_lock, name):
#     for item in values:
#         print(f"{name} waiting for lock")
#         start_lock.acquire()
#         print(item)
#         end_lock.release()

# lock1 = Lock()
# lock2 = Lock()
# lock2.acquire()

# thread1 = Thread(target=print_values, args=([1, 3, 5], lock1, lock2, "zmn"))
# thread2 = Thread(target=print_values, args=([2, 4], lock1, lock2, "zmn2"))


# thread1.start()
# thread2.start()


#######################


# def start_game(preq=[]):
#     print("waiting to start game.")

#     for t in preq:
#         t.join()
    
#     print("Started game!")

# def load_assets():
#     sleep(2)
#     print("assets loaded!")

# def load_player():
#     sleep(1)
#     print("playes loaded!")


# load_assets_thread = Thread(target=load_assets)
# load_player_thread = Thread(target=load_player)
# preq = [load_assets_thread, load_player_thread]
# start_game_thread = Thread(target=start_game, args=(preq,))

# load_assets_thread.start()
# load_player_thread.start()
# start_game_thread.start()


#######################

def wait_on_thread(threads):
    sleep(1)
    for thread in threads:
        thread.join()
    print("ran")

threads = []

t1 = Thread(target=wait_on_thread, args=(threads,))
t2 = Thread(target=wait_on_thread, args=([t1],))
threads.append(t2)

t1.start()
t2.start()