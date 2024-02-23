from time import perf_counter, sleep
import threading
import multiprocessing


def cpu_bound_task(num_jobs):
    x = 0
    for i in range(num_jobs):
        x += 1


def io_bound_task(sleep_time):
    sleep(sleep_time)


def test_io_bound_thread(num_thread, sleep_time=4):

    threads = []

    start = perf_counter()
    for _ in range(num_thread):
        t = threading.Thread(target=io_bound_task, args=(sleep_time / num_thread,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    runtime = perf_counter() - start

    print(f"* [{num_thread}] thread runtime: {runtime:.4f} sec")


def test_cpu_bound_thread(num_thread, num_jobs=1000000):

    threads = []

    start = perf_counter()
    for _ in range(num_thread):
        t = threading.Thread(target=cpu_bound_task, args=(num_jobs // num_thread,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    runtime = perf_counter() - start

    print(f"* [{num_thread}] thread runtime: {runtime:.4f} sec")


def test_io_bound_process(num_proc, sleep_time=4):

    procs = []

    start = perf_counter()
    for _ in range(num_proc):
        p = multiprocessing.Process(target=io_bound_task, args=(sleep_time / num_proc,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
    runtime = perf_counter() - start

    print(f"* [{num_proc}] thread runtime: {runtime:.4f} sec")


def test_cpu_bound_process(num_proc, num_jobs=1000000):

    procs = []

    start = perf_counter()
    for _ in range(num_proc):
        p = multiprocessing.Process(target=cpu_bound_task, args=(num_jobs // num_proc,))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
    runtime = perf_counter() - start

    print(f"* [{num_proc}] thread runtime: {runtime:.4f} sec")


def main():

    test_threads = [1, 2, 4, 8]
    num_jobs = 10000000

    print(f"---- START MULTI THREAD TEST ----")
    print(f"CPU BOUND:")
    for num_thread in test_threads:
        test_cpu_bound_thread(num_thread, num_jobs)

    print(f"\nI/O BOUND:")
    for num_thread in test_threads:
        test_io_bound_thread(num_thread)

    print(f"\n---- START MULTI PROCESS TEST ----")
    print(f"CPU BOUND:")
    for num_thread in test_threads:
        test_cpu_bound_process(num_thread, num_jobs)

    print(f"\nI/O BOUND:")
    for num_thread in test_threads:
        test_io_bound_process(num_thread)


if __name__ == "__main__":
    main()
