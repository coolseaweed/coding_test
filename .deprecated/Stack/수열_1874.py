
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
        return len(self.stack_items)





##################
## example code ##
##################


num_command  = int(input().strip())

n_list = list(range(1,num_command+1))



stacker = stack()

command = []


while num_command:

    command.append(int(input().strip())) 
    
    num_command -= 1



result = []

for c in command:

    check = True
    out = False

    while check:

        if stacker.top() == c:
            stacker.pop()
            result.append('-')
            check = False
        elif (len(n_list)<1) and (stacker.isEmpty() == False):
            result = 'NO'
            out = True
            break
        else:
            stacker.push(n_list[0])
            del n_list[0]
            result.append('+')


    if out:
        break

if out:
    print(result)
else:
    for i in result:
    
        print(i)