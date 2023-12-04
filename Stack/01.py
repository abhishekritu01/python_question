
class Node:
    def __init__(self,value):
        self.data = value
        self.next =None


class Stack:
    def __init__(self):
        self.top =None


    def isempty(self):
        return self.top == None  

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)    
            temp = temp.next

    def peak(self):        
        if (self.isempty()):
            return "stack is empty"
        else:
            return self.top.data
        
    def pop(self):
        if(self.isempty()):
            return "stack is empty"
        else:
            self.top = self.top.next


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
# s.isempty()
# print(s.isempty())
# print(s.traverse())
# print(s.peak())
print(s.pop())


