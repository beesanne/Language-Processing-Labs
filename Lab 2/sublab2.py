class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def traverserec(self):
        temp = self.head
        if temp == None:
            return
        print(temp.data, ", ", end=" ")
        traverserec(temp.next)

    def traversewithloop(self):
        temp = self.head
        while (temp):
            print(temp.data, ", ", end=" ")
            temp = temp.next
 

n = 1
list = LinkedList()
while n <= 10:
    x = int(input("enter a number: "))
    list.add(x)
    n += 1
list.traversewithloop()
list.traverserec()