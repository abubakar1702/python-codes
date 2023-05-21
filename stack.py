stack = []


def push():
    number = input("Enter any number")
    stack.append(number)
    print(number)


def pop_number():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Removed element ", e)
        print(stack)


while True:
    print("Select the operation: 1.Push, 2.Pop, 3.Quit")
    select = int(input())
    if select == 1:
        push()
    elif select == 2:
        pop_number()
    elif select == 3:
        break
    else:
        print("Inserted wrong number!")
