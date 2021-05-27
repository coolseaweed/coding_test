from collections import deque

queue = deque(['Mon','Tue','Wed'])
queue.append('Thu')

print(queue)

queue.appendleft('Sun')
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)