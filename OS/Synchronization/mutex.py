import time
from concurrent.futures import ThreadPoolExecutor
import threading


class FakeDataStore:

    def __init__(self) -> None:
        self.value = 0  # stack area
        self._lock = threading.Lock()

    def update(self, n):
        print(f"Thread {n}: starting update")

        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        print(f"Thread {n}: finished update (value: {self.value})")

    def mutex_update(self, n):
        print(f"Thread {n}: starting update")

        self._lock.acquire()
        print(f"Thread {n}: Locked")

        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        print(f"Thread {n}: finished update (value: {self.value})")
        self._lock.release()

    def sema_update(self, n):
        print(f"Thread {n}: starting update")

        self._sema.acquire()
        print(f"Thread {n}: had semaphore")

        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        print(f"Thread {n}: finished update (value: {self.value})")
        self._sema.release()


if __name__ == "__main__":

    store = FakeDataStore()
    N_THREAD = 5
    N_JOB = 5

    print(f"[TEST] multi-thread update\n* Start value: {store.value}")
    with ThreadPoolExecutor(max_workers=N_THREAD) as executor:
        for n in range(N_JOB):
            executor.submit(store.update, n)
    print(f"* End value: {store.value} (Expected: {N_JOB})\n")

    store.value = 0
    print(f"[TEST] mutex multi-thread update\n* Start value: {store.value}")
    with ThreadPoolExecutor(max_workers=N_THREAD) as executor:
        for n in range(N_JOB):
            executor.submit(store.mutex_update, n)

    print(f"* End value: {store.value} (Expected: {N_JOB})\n")
