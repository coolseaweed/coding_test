
import sys

input = sys.stdin.readline

num_command  = int(input().strip())

stack = []


while num_command:

    c = input().strip()
    commands = c.split(' ')

    if commands[0] == 'push':
        stack.append(int(commands[1]))

    elif commands[0] == 'top':

        if len(stack) < 1:
            print(-1)
        else:
            print(stack[-1])


    elif commands[0] == 'size':

        print(len(stack))

    elif commands[0] == 'pop':
        if len(stack) < 1:
            print(-1)

        else :
            print(stack[-1])
            del stack[-1]


    elif commands[0] == 'empty':

        if not stack:
            print(1)
        else:
            print(0)

    else:
        continue


    num_command -= 1

















