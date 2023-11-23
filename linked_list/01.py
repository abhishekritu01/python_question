
# class Node:

#     def __init__(self,value):
#         self.data = value
#         self.next = None


# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next=b
# b.next =c

# print(a.next)


# ------------------

# class Node:

#     def __init__(self,value):
#         self.data = value
#         self.next = None


# class LinkedList:

#     def __init__(self):
        
#         # create empty linked list
#         self.head = None
#         self.n = 0
    
#     def __len__(self):

#         return self.n  #no nodes of linked list 

# L = LinkedList()

# print(len(L))



# --------------------------

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

L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(len(L))  # Output: 4

print(L)




        

