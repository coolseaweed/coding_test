import gc
from time import perf_counter

gc.set_debug(True)


class Link:
    def __init__(self, next_link, value) -> None:
        self.next_link = next_link
        self.value = value

    def __repr__(self):
        return self.value


def main():

    l = Link(None, "Main Link")
    my_list = []
    start = perf_counter()
    for i in range(2000):
        l_temp = Link(l, value="L")
        my_list.append(l_temp)
    runtime = perf_counter() - start
    print(f"total runtime: {runtime:.4f} sec")


if __name__ == "__main__":
    main()
