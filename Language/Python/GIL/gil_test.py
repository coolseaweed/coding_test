from time import perf_counter, sleep
import threading


def cpu_bound_task(num_jobs):
    x = 0
    for i in range(num_jobs):
        x += 1


def io_bound_task(sleep_time):
    sleep(sleep_time)


def test_io_bound(num_thread, sleep_time=8):

    threads = []

    start = perf_counter()
    for _ in range(num_thread):
        t = threading.Thread(target=io_bound_task, args=(sleep_time // num_thread,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    runtime = perf_counter() - start

    print(f"* [{num_thread}] thread runtime: {runtime:.2f} sec")


def test_cpu_bound(num_thread, num_jobs=1000000):

    threads = []

    start = perf_counter()
    for _ in range(num_thread):
        t = threading.Thread(target=cpu_bound_task, args=(num_jobs // num_thread,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    runtime = perf_counter() - start

    print(f"* [{num_thread}] thread runtime: {runtime:.2f} sec")


def main():

    test_threads = [1, 2, 4, 8]

    print(f"---- START CPU BOUND TEST ----")
    for num_thread in test_threads:
        test_cpu_bound(num_thread)
    print(f"---- END TEST ----\n")

    print(f"---- START I/O BOUND TEST ----")
    for num_thread in test_threads:
        test_io_bound(num_thread)
    print(f"---- END TEST ----")


if __name__ == "__main__":
    main()
