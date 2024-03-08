import threading
from time import sleep, perf_counter

SLEEP_TIME = 0.5


def process_item(item, semaphore):
    semaphore.acquire()  # acquire the semaphore
    try:
        sleep(SLEEP_TIME)  # simulate some processing time
        # print(f"Processing item {item}")  # process the item
    finally:  # Make sure we always release the semaphore
        semaphore.release()  # release the semaphore


def test_semaphore(items, n_sema):
    semaphore = threading.Semaphore(value=n_sema)
    threads = [
        threading.Thread(
            target=process_item,
            args=(item, semaphore),
        )
        for item in items
    ]

    [thread.start() for thread in threads]  # start all threads
    t1_start = perf_counter()
    [thread.join() for thread in threads]  # wait for all threads to finish
    runtime = perf_counter() - t1_start
    print(f"[# SEMA {n_sema}] runtime: {runtime:.2f} sec")


if __name__ == "__main__":
    N_THREAD = 8
    SEMAPHORES = [1, 2, 4, 8]
    items = [1, 2, 3, 4, 5, 6, 7, 8]

    print(f"* Serial processing time: {SLEEP_TIME * len(items)} sec\n* Num Thread: {N_THREAD}")
    for sema in SEMAPHORES:
        test_semaphore(items, sema)

# create a list of threads to process the items
