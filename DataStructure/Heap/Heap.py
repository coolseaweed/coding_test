class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        # set 0 index as `None` value to use 1 index as root
        self.heap.append(None)
        self.flag = 0

    def __len__(self):
        return len(self.heap) - 1

    def _swap(self, lpos, rpos):
        self.heap[lpos], self.heap[rpos] = self.heap[rpos], self.heap[lpos]

    def insert(self, data) -> None:
        self.heap.append(data)
        curr_idx = len(self.heap) - 1

        while curr_idx != 1:
            parent_idx = curr_idx // 2
            if self.heap[curr_idx] > self.heap[parent_idx]:
                self._swap(curr_idx, parent_idx)
                curr_idx = parent_idx
            else:
                break

    def _heapify(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        max_idx = idx

        if left_idx <= len(self.heap) - 1 and self.heap[max_idx] < self.heap[left_idx]:
            max_idx = left_idx

        if right_idx <= len(self.heap) - 1 and self.heap[max_idx] < self.heap[right_idx]:
            max_idx = right_idx

        if max_idx != idx:
            self._swap(idx, max_idx)
            self._heapify(max_idx)

    def pop(self):

        if len(self.heap) <= 1:
            return None

        self._swap(1, -1)  # swap root and last
        root = self.heap.pop()
        self._heapify(1)

        return root

    def show(self):

        print(" -> ".join([str(x) for x in self.heap]))


if __name__ == "__main__":
    heap = MaxHeap()
    items = [1, 100, 3, 19, 17, 36, 2, 7, 25]

    print(f"[INSERT PROCESSING]")
    for item in items:
        print(f"insert: {item}")
        heap.insert(item)
        heap.show()

    res = []
    print(f"\n[POP PROCESSING]")
    while heap:
        val = heap.pop()
        print(f"pop: {val}")
        heap.show()
        res.append(val)

    print(f"result: {res}")
