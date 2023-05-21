import collections

queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.appendleft(40)

queue.popleft()
print(queue)