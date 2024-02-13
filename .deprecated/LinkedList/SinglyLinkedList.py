
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr  = curr.next

    def appendleft(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, key):
        curr = self.head

        if self.head is not None:
            if self.head.data == key:
                self.head = curr.next
                curr = None
                return
        
        while curr is not None:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next

        if curr == None: return

        prev.next = curr.next
        curr = None


s_list = SLinkedList()
s_list.append("Mon")
s_list.append("Tue")
s_list.append("Wed")
s_list.show()

print('\n--------- [ appendleft check] --------')
s_list.appendleft('Sun')
s_list.show()


print('\n--------- [ append check ] --------')
s_list.append('Thu')
s_list.show()

print('\n--------- [ remove check ] --------')
s_list.remove('Tue')
s_list.show()

print('\n--------- [ remove check ] --------')
s_list.remove('Mon')
s_list.show()
