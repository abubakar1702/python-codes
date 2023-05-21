queue = []


def enqueue():
    element = input("Enter element:")
    queue.append(element)
    print(element, "added to queue")


def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        n = queue.pop(0)
        print("Removed", n)


def display():
    print(queue)


while True:
    print("Select option: 1. Add, 2. Remove, 3. Quit")
    n = int(input())
    if n == 1:
        enqueue()
    elif n == 2:
        dequeue()
    elif n == 3:
        break
    else:
        print("Enter a valid number")
display()
