from time import time
import threading


def loop(num=50000000):

    for i in range(num):
        pass


def test_cpu_bound(num=50000000):

    # single thread
    start = time()
    loop(num)
    loop(num)
    st_time = time() - start

    # multi thread
    start = time()
    thread1 = threading.Thread(target=loop, args=(num,))
    thread2 = threading.Thread(target=loop, args=(num,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    mt_time = time() - start

    report = f"---- CPU BOUND TEST ----\n* single thread runtime: {st_time:.4f} sec\n* multi thread runtime: {mt_time:.4f} sec\n"
    print(report)


def main():
    test_cpu_bound()


if __name__ == "__main__":
    main()
