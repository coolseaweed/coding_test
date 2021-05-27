
class MinHeap:
    def __init__(self, A=[]):
        self.queue = [None] + A[:]
        for i in range(len(self.queue)//2,0,-1):
            self.minHeapify(i)
    
    @staticmethod
    def parent(index):  return index//2

    @staticmethod
    def leftchild(index): return index*2

    @staticmethod
    def rightchild(index): return index*2+1

    def swap(self,i,parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, data):
        self.queue.append(data)
        i = len(self.queue)-1
        while i > 1:
            parent = self.parent(i)
            if self.queue[i] < self.queue[parent]:
                self.swap(i,parent)
                i = parent
            else: break

    def remove(self):
        self.swap(1,len(self.queue)-1)
        e = self.queue.pop(-1)
        self.minHeapify(1)
        return e
    def minHeapify(self,i):
        left = self.leftchild(i)
        right = self.rightchild(i)
        smallest = i
        if left <= len(self.queue) -1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue)-1 and self.queue[right] < self.queue[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)


class MaxHeap:
    def __init__(self, A=[]):
        self.queue = [None] + A[:]
        for i in range(len(self.queue)//2,0,-1):
            self.maxHeapify(i)
    
    @staticmethod
    def parent(index):  return index//2

    @staticmethod
    def leftchild(index): return index*2

    @staticmethod
    def rightchild(index): return index*2+1

    def swap(self,i,parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, data):
        self.queue.append(data)
        i = len(self.queue)-1
        while i > 1:
            parent = self.parent(i)
            if self.queue[i] > self.queue[parent]:
                self.swap(i,parent)
                i = parent
            else: break

    def remove(self):
        self.swap(1,len(self.queue)-1)
        e = self.queue.pop(-1)
        self.maxHeapify(1)
        return e

    def maxHeapify(self,i):
        left = self.leftchild(i)
        right = self.rightchild(i)
        largest = i
        if left <= len(self.queue) -1 and self.queue[left] > self.queue[largest]:
            largest = left
        if right <= len(self.queue)-1 and self.queue[right] > self.queue[largest]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.maxHeapify(largest)







import random

print('\n\n@@@@@@@@@@@@@@@@@@ here is min heap @@@@@@@@@@@@@@@@@@@@@@')

minheap = MinHeap()
elements = [32,35,20,6,31,40,17,1,3,4]

for i in range(10):
    e = elements[i]
    minheap.insert(e)
    print(minheap.queue)
print('-------------------------')
for _ in range(10):
    e = minheap.remove()
    print(minheap.queue, e)


print('\n\n@@@@@@@@@@@@@@@@@@ here is max heap @@@@@@@@@@@@@@@@@@@@@@')

maxheap = MaxHeap()
elements = [32,35,20,6,31,40,17,1,3,4]

for i in range(10):
    e = elements[i]
    maxheap.insert(e)
    print(maxheap.queue)
print('-------------------------')
for _ in range(10):
    e = maxheap.remove()
    print(maxheap.queue, e)


