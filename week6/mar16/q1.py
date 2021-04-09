class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.new = None

    # adding new item at the end
    def append(self, data):
        node = Node(data)

        # if list is empty
        if self.new is None:
            self.new = node
            return

        n = self.new

        # traversing to last node
        while n.next is not None:
            n = n.next

        n.next = node

    # traversing and printing list
    def traverse(self):
        # if list is empty
        if self.new is None:
            print("List has no element")
            return
        else:
            n = self.new
            while n is not None:
                print(n.data, end=' ')
                n = n.next

    # deleting specific item 
    def delete(self, x):
        # is list is empty
        if self.new is None:
            print("The list has no element to delete")
            return

        # deleting and connecting with next node 
        if self.new.data == x:
            self.new = self.new.next
            return

        n = self.new
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

        if n.next is None:
            print("data not found in the list")
        else:
            n.next = n.next.next

# main program
if __name__ == "__main__":
    mylist = LinkedList()

    mylist.append(10)
    mylist.append(20)
    mylist.append(30)
    mylist.append(40)
    mylist.append(50)

    print("\nlist is: ")
    mylist.traverse()

    mylist.delete(30)

    print("\n\nafter deleting list is: ")
    mylist.traverse()
