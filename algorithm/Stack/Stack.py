class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, data):

        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) <= 0: return print('There are no elements in stack')
        else:  return self.stack.pop()
    def show(self):
        print(self.stack)

stack = Stack()
stack.push('Mon')
stack.push('Tue')
stack.push('Wed')
stack.push('Thu')
stack.show()
print('-----------------')
stack.pop()
stack.show()

