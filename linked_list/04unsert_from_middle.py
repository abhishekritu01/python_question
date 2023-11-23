class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''

        while curr is not None:
            result += str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    # insert from the last node
    def append(self, value):
        new_node = Node(value)

        if self.head is None:  # check for an empty linked list
            self.head = new_node
            self.n += 1
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        # you are at the last node
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        # case1: break loop curr value never None
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'item not found'
        # case2: item not found curr --> None


L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

L.append(5)

print("Length:", len(L))
print("Original List:", L)

L.insert_after(1, 200)
print("Updated List:", L)
