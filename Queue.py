# Queue: First in first out

queue = []

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

# [10,20,30,40,50]

queue.pop(0)
# 10 will be removed cause 10 is the 1st item
# now the queue would look like [20,30,40,50]
# if we write pop(0) again, 20 will be removed
# cause 20 is now on index 0
queue.pop(0)

print(queue)

# output: [30,40,50]
