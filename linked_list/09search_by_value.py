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


    def search(self,item): 
        curr = self.head
        pos =0

        while curr !=None:
            if curr.data ==item:
                return pos
            
            curr = curr.next
            pos = pos + 1

        return 'Not Found'    



L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

# L.insert_head(31).display()

print(L.search(13))
