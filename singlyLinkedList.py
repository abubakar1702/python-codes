class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.ref is None:
                    break
                last_node = last_node.ref
            last_node.ref = new_node

    def before(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # def insert_after(self, data, x):

    #     temp = self.head

    #     while temp != None:
    #         if x == temp.data:
    #             break
    #     if temp is None:
    #         print("Empty")
    #     else:
    #         new_node = Node(data)
    #         new_node.ref = temp.ref
    #         temp.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before2(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        prev_node = self.head
        curr_node = self.head.ref

        while curr_node is not None:
            if curr_node.data == x:
                new_node = Node(data)
                new_node.ref = curr_node
                prev_node.ref = new_node
                return
            prev_node = curr_node
            curr_node = curr_node.ref

        print("Node is not found")

    def printNodes(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.ref


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
nodeX = Node(100)

linkedlist = LinkedList()
linkedlist.insertNode(node1)
linkedlist.insertNode(node2)
linkedlist.insertNode(node3)
linkedlist.before(100)

# linkedlist.insert_after(35, 20)
linkedlist.add_before(45, 20)
linkedlist.printNodes()
