class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def peak(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.top.data

    def pop(self):
        if self.isempty():
            return "stack is empty"
        else:
            popped_value = self.top.data
            self.top = self.top.next
            return popped_value


    def reverse_string(text):
        s = Stack()
        for i in text:
            s.push(i)

        reverse_str = ""

        while not s.isempty():
            reverse_str += s.pop()

        print(reverse_str)

    @staticmethod
    def text_editor(text, pattern):
        u = Stack()
        r = Stack()

        for i in text:
            u.push(i)

        res = ""
        for i in pattern:
            if i == 'u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)
        res =''


        while not u.isempty():
            res = u.pop() + res
            print(res)


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
# print(s.pop())
Stack.reverse_string('hello')

Stack.text_editor("kolkata", "uuurr")
