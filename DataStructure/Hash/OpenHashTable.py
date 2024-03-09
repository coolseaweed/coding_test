class OpenHashTable:
    """Seperate Chaining:
    use extra storage (LinkedList) when collision is happend:
    """

    def __init__(self, size: int) -> None:
        self.hash_table = [None] * size
        self.size = size

    def __hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_addr = self.__hash_function(hash(key))
        if self.hash_table[hash_addr]:
            for a in range(len(self.hash_table[hash_addr])):
                if self.hash_table[hash_addr][a][0] == key:
                    self.hash_table[hash_addr][a][1] = value
                    return
            self.hash_table[hash_addr].append([key, value])
        else:
            self.hash_table[hash_addr] = [[key, value]]

    def get(self, key):
        hash_addr = self.__hash_function(hash(key))
        if self.hash_table[hash_addr]:
            for a in range(len(self.hash_table[hash_addr])):
                if self.hash_table[hash_addr][a][0] == key:
                    return self.hash_table[hash_addr][a][1]

        return None

    def show(self):
        print(self.hash_table)


if __name__ == "__main__":

    items = [
        ("tom", "smart"),
        (1, 2),
        (2, 4),
        (3, 9),
        ("rami", "genious"),
    ]

    hash_table = OpenHashTable(2)

    print(f"[INSERT]")
    for k, v in items:
        hash_table.insert(k, v)
    hash_table.show()

    print(f"\n[GET]")
    for k, v in items:
        val = hash_table.get(k)
        assert val == v
        print(f"k: {k} -> val: {val}")
