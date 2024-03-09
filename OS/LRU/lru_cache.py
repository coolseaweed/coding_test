class LRUCache:

    class Node:
        def __init__(self, key: int, val: int, prev=None, next=None) -> None:
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self, max_size: int) -> None:
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = max_size
        self.cache = {}

    def _delete(self, node: Node):
        node_after = node.next
        node_before = node.prev
        node_before.next = node_after
        node_after.prev = node_before

    def _add(self, node: Node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node

    def get(self, key):
        print(f"Trying to get key: {key}")
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            del self.cache[key]
            self._delete(node)
            self._add(node)
            self.cache[key] = self.head.next
            print(f"Hit!")
            return val
        print(f"Miss!")
        return None

    def put(self, key: int, val: int) -> None:

        if key in self.cache:
            curr = self.cache[key]
            del self.cache[key]
            self._delete(curr)

        if len(self.cache) == self.max_size:
            del self.cache[self.tail.prev.key]
            self._delete(self.tail.prev)
        self._add(self.Node(key, val))
        self.cache[key] = self.head.next

    def print_all(self):
        node = self.head.next
        while node.key:
            print(f"{node.key}", end="")
            node = node.next
            if node.key:
                print(" -> ", end="")
        print(f"")


if __name__ == "__main__":
    lru_cache = LRUCache(11)
    inputs = [(1, 1), (2, 2), (1, 1), (3, 3), (4, 4), (1, 1), (5, 5), (4, 4)]
    print(f"PUT PROCESS:")
    for k, v in inputs:
        lru_cache.put(k, v)
        lru_cache.print_all()
    print("\nGET PROCESS:")
    lru_cache.get(1)
    lru_cache.print_all()
    lru_cache.get(11)
    lru_cache.print_all()
    lru_cache.get(2)
    lru_cache.print_all()
