import asyncio
from time import perf_counter


def cpu_bound(num_jobs):
    x = 0
    for i in range(num_jobs):
        x += 1
    return x


async def main():
    N_JOBS = 100000000
    N_THREADS = 4
    loop = asyncio.get_running_loop()

    # 1. default
    start = perf_counter()
    result = await loop.run_in_executor(None, cpu_bound, N_JOBS)
    elapsed = perf_counter() - start
    print(f"default thread pool: {result}")
    print(f"elapsed: {elapsed:.2f} sec")

    # 2. futures
    start = perf_counter()
    tasks = [loop.run_in_executor(None, cpu_bound, N_JOBS // N_THREADS) for i in range(N_THREADS)]
    results = await asyncio.gather(*tasks)
    elapsed = perf_counter() - start
    print(f"default thread pool: {sum(results)}")
    print(f"elapsed: {elapsed:.2f} sec")


if __name__ == "__main__":
    asyncio.run(main())
