class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # create an empty linked list
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n  # no. of nodes in the linked list

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

        return self  # Return the linked list after insertion

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def search(self, item):
        curr = self.head
        pos = 0

        while curr is not None:
            if curr.data == item:
                return pos

            curr = curr.next
            pos += 1

        return 'Not Found'

    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr is not None:
            if pos == index:
                return curr.data

            curr = curr.next
            pos += 1

        return None


L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(L[10])
