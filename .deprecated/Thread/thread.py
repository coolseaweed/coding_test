import threading,time




##########
# 예제 1 #
##########

class MyThread1(threading.Thread):
    def run(self):
        for i in range(10):
            print('id={} --> {}'.format(self.getName(),i))
            time.sleep(0)


threads = []

for i in range(2):
    th = MyThread1()
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print('exit')



##########
# 예제 2 #
##########

g_count = 0
class MyThread2(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            # lock
            lock.acquire()
            g_count += 1
            time.sleep(0.1)
            print('[{}] g_count is: {}'.format(self.getName(),g_count))

            # unlock
            lock.release()


# Lock 객체 생성
lock = threading.Lock()

threads = []

for i in range(2):
    th = MyThread2()
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print(f'total count is {g_count}')
print('exit')

