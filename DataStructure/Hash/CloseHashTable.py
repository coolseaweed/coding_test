class CloseHashTable:
    """
    Linear Probing:
    - when collision is happend, search empty space
    - still collison can be happend
    """

    def __init__(self, size: int) -> None:
        self.hash_table = [None] * size
        self.size = size

    def __hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_addr = self.__hash_function(hash(key))
        if self.hash_table[hash_addr]:
            for a in range(hash_addr, len(self.hash_table)):
                if not self.hash_table[a]:
                    self.hash_table[a] = [key, value]
                    break
                # overwrite
                elif self.hash_table[a][0] == key:
                    self.hash_table[a] = [key, value]
                    break
        else:
            self.hash_table[hash_addr] = [key, value]

    def get(self, key):
        hash_addr = self.__hash_function(hash(key))
        if self.hash_table[hash_addr]:
            for a in range(hash_addr, len(self.hash_table)):
                if self.hash_table[a][0] == key:
                    return self.hash_table[a][1]

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

    hash_table = CloseHashTable(8)

    print(f"[INSERT]")
    for k, v in items:
        hash_table.insert(k, v)
    hash_table.show()

    print(f"\n[GET]")
    for k, v in items:
        val = hash_table.get(k)
        assert val == v, f"val: {val} (expect: {v})"
        print(f"k: {k} -> val: {val}")
