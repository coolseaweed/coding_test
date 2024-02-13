import threading,time


##########
# 예제 1 #
##########

# 세마포어 객체 생성, 한번에 실행될 쓰레드를 3개로 제한
sem = threading.Semaphore(3)

class RestrictedArea(threading.Thread):
    def run(self):
        # 쓰레드가 3개만 동작하는 걸 쉽게 확인 할 수 있도록 쓰레드의 작업을 3번 반복
        # 결과를 확인하면 하번에 3개의 쓰레가 3번 동작하는 것을 확인.
        for i in range(3):
            msg = 'Threading Semaphore TEST : {}'.format(self.getName())
            sem.acquire()

            # 3개의 쓰레드만이 존재가능한 영역
            print(msg)
            time.sleep(2)

            sem.release()


def test(name):
    for i in range(3):
        msg = 'Threading Semaphore TEST : {}'.format(name)

        # 3개의 쓰레드만이 존재가능한 영역
        print(msg)
        time.sleep(2)

        sem.release()


threads = []


# for i in range(10):
#     threads.append(RestrictedArea())

# for th in threads:
#     th.start()


for i in range(10):
    th = threading.Thread(target=test,args=(i,))
    th.start()
    threads.append(th)


for th in threads:
    th.join()

print('Finished All Threading')


##########
# 예제 2 #
##########

