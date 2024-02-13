class Queue:
    def __init__(self):
        self.queue = list()
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        return self.queue.pop(0)
    def show(self):
        print(self.queue)

queue = Queue()
queue.push('Mon')
queue.push('Tue')
queue.push('Wed')
queue.show()
print('-------------')
queue.pop()
queue.show()
