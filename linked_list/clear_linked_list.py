# class Node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.n = 0

#     def __len__(self):
#         return self.n

#     def insert_head(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#         self.n += 1

#     def __str__(self):
#         curr = self.head
#         result = ''

#         while curr is not None:
#             result += str(curr.data) + '->'
#             curr = curr.next

#         return result[:-2]

#     def append(self, value):
#         new_node = Node(value)

#         if self.head is None:
#             self.head = new_node
#             self.n += 1
#             return

#         curr = self.head

#         while curr.next is not None:
#             curr = curr.next

#         curr.next = new_node
#         self.n += 1

#     def insert_after(self, after, value):
#         new_node = Node(value)

#         curr = self.head

#         while curr is not None:
#             if curr.data == after:
#                 break
#             curr = curr.next

#         if curr is not None:
#             new_node.next = curr.next
#             curr.next = new_node
#         else:
#             return 'item not found'

#     def clear(self):
#         self.head = None
#         self.n = 0

#     def delete_head(self):
#         if self.head is not None:
#             self.head = self.head.next
#             self.n -= 1
#         else:
#             print("Cannot delete from an empty list.")


#     def pop(self):
#         curr = self.head

#         if curr.next == None:
#             self.delete_head()

        
#         while curr.next.next != None: 
#             curr = curr.next

#             # curr is 2nd last node
#         curr.next =None
#         self.n -= 1

#     def remove_by_value(self,value):
#         curr = self.head

#         while curr.next !=None:
#             if curr.next.data == value:
#                 break
#             curr=curr.next

#             # 2 case   1 item found       2. item not found

#             if curr.next == None:
#                 return 'Not found'
            
#             else:
#                 # bypass the connection
#                 curr.next = curr.next.next

            





    



    






# L = LinkedList()
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(3)
# L.insert_head(4)

# # L.append(5)

# # L.delete_head()

# # print("pop",L.pop())
# print("pop",L.remove_by_value(2))

# # print("Length:", len(L))
# # print("Updated List:", L)





# --------------





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

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.n += 1
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
            self.n -= 1
        else:
            print("Cannot delete from an empty list.")

    def pop(self):
        if self.head is None:
            print("Cannot pop from an empty list.")
            return None

        if self.head.next is None:
            # If there is only one element in the list
            popped_value = self.head.data
            self.head = None
            self.n -= 1
            return popped_value

        curr = self.head

        while curr.next.next is not None:
            curr = curr.next

        popped_value = curr.next.data
        curr.next = None
        self.n -= 1
        return popped_value

    def remove_by_value(self, value):
        curr = self.head

        while curr.next is not None:
            if curr.next.data == value:
                # item found, bypass the connection
                curr.next = curr.next.next
                return
            curr = curr.next

        # item not found
        print("Not found")


# Example usage:
L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

# Uncomment the following lines to test other operations
# L.append(5)
# L.delete_head()
# print("pop", L.pop())
L.remove_by_value(2)

print("Length:", len(L))
print("Updated List:", L)
