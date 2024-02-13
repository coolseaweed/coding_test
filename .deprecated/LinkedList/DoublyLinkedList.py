
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def appendleft(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


    def showforward(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr  = curr.next

    def showbackward(self):
        curr = self.tail
        while curr is not None:
            print(curr.data)
            curr  = curr.prev


    def remove(self, key):
        curr = self.head

        if self.head is not None:
            if self.head.data == key:
                self.head = curr.next
                self.head.prev = None
                curr = None
                return
        
        while curr is not None:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next

        if curr == None: return

        prev.next = curr.next
        curr.next.prev = prev
        curr = None


d_list = DLinkedList()
d_list.append("Mon")
d_list.append("Tue")
d_list.append("Wed")
d_list.append("Thu")
d_list.showforward()
print('-----------------------')
d_list.showbackward()

print('\n----------- [ head & tail check ] ----------')
print(d_list.head.data)
print(d_list.head.next.data)
print(d_list.tail.prev.data)
print(d_list.tail.data)


print('\n----------- [ appendleft check ] ----------')
d_list.appendleft("Sun")
d_list.showforward()
print('-----------------------')
d_list.showbackward()


print('\n----------- [ remove check ] ----------')
d_list.remove("Wed")
d_list.showforward()
print('-----------------------')
d_list.showbackward()



print('\n----------- [ remove check ] ----------')
d_list.remove("Mon")
d_list.showforward()
print('-----------------------')
d_list.showbackward()



print('\n----------- [ remove check ] ----------')
d_list.remove("sadasd")
d_list.showforward()
print('-----------------------')
d_list.showbackward()
