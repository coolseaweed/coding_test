
import sys

input = sys.stdin.readline


class stack:

    def __init__(self):
        self.stack_items=[]
    
    def pop(self):

        if len(self.stack_items) < 1:
            #print("Stack is empty!")
            return -1

        result = self.stack_items[-1]
        del self.stack_items[-1]
        return result

    def push(self,x):
        self.stack_items.append(x)
    
    def isEmpty(self):
        return not self.stack_items

    def show(self):
        print(self.stack_items)

    def top(self):

        if len(self.stack_items) < 1:
            return -1
        else:
            return self.stack_items[-1]

    def size(self):
        print(len(self.stack_items))




def check_PS(PS):
    
    stacker = stack()

    for c in PS:
        
        if stacker.isEmpty():
            stacker.push(c)
        elif (c == ')') and (stacker.top() == '('):
            stacker.pop()
        else:
            stacker.push(c)
        

    if stacker.isEmpty():
        print('YES')
    else:
        print('NO')


##################
## example code ##
##################



num_command  = int(input().strip())

while num_command:

    PS = input().strip()
    
    check_PS(PS)

    num_command -= 1


