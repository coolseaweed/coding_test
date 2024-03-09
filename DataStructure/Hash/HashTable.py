class HashTable:
    """collison can be happend"""

    def __init__(self, size: int) -> None:
        self.hash_table = [None] * size
        self.size = size

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_value = self._hash_function(hash(key))
        old_value = self.hash_table[hash_value]
        if old_value:
            print(f"[WARNING] collision! (key: {key}, val:{value}, old_val: {old_value})")
        else:
            self.hash_table[hash_value] = value

    def get(self, key):
        hash_value = self._hash_function(hash(key))
        return self.hash_table[hash_value]

    def show(self):
        print(self.hash_table)


if __name__ == "__main__":
    hash_table = HashTable(8)
    hash_table.insert("tom", "smart")
    hash_table.insert(1, 2)
    hash_table.insert(2, 4)
    hash_table.insert(3, 9)
    hash_table.insert("rami", "genious")

    value = hash_table.get("tom")
    hash_table.show()
