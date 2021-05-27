
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





def check_PS(PS):
    
    stacker = stack()
    temp = ''


    check_A = 0
    check_B = 0



    for c in PS:
        if c == '(' or c == ')':
            check_A += 1
        elif c == '[' or c == ']':
            check_B += 1

        #print(check_A, check_B)

    if (check_A%2 + check_B%2) == 0:

        for c in PS:

            if stacker.isEmpty():
                stacker.push(c)


            elif c == '(' :
                if  stacker.top() == '(' :
                    temp += '2*('
                elif stacker.top()=='[':
                    temp += '3*('

                elif stacker.top() == ')' or stacker.top()==']':
                    stacker.pop()
                    stacker.pop()                
                    temp += '+'

                stacker.push(c)



            elif c == '[':
                if  stacker.top() == '(' :
                    temp += '2*('
                elif stacker.top()=='[':
                    temp += '3*('

                elif stacker.top() == ')' or stacker.top()==']':
                    stacker.pop()
                    stacker.pop()                
                    temp += '+'

                stacker.push(c)



            elif c == ')':
                if stacker.top() == '(' :
                    temp += '2'

                elif stacker.top() == ']' or stacker.top() == ')':
                    stacker.pop()
                    stacker.pop()
                    temp += ')'
                elif stacker.top() == '[':
                    return 0

                stacker.push(c)


            elif c == ']':
                if stacker.top() == '[' :
                    temp += '3'

                elif stacker.top() == ']' or stacker.top() == ')':
                    stacker.pop()
                    stacker.pop()
                    temp += ')'
                elif stacker.top() == '(':
                    return 0
                stacker.push(c)



            # print('---------------------')
            # stacker.show()
            # print(f'num is:{temp}')

        try:
            return eval(temp)

        except SyntaxError:
            return 0


    
    else :
        return 0




##################
## example code ##
##################




PS = input().strip()

result = check_PS(PS)

print(result)

