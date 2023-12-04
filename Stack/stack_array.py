# class Stack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = [None] * self.size
#         self.top = -1

#     def is_full(self):
#         return self.top == self.size - 1

#     def push(self, value):
#         if self.is_full():
#             return "Overflow"
#         else:
#             self.top += 1
#             self.stack[self.top] = value

# s = Stack(3)
# s.push(4)
# s.push(3)
# s.push(2)
# s.push(2)
# s.push(2)  # This will result in "Overflow"

# print(s.stack)



# --------------------------------


class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            return "Empty"
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data

s = Stack(3)
s.push(4)
s.push(3)
s.push(2)
# s.push(2)
# s.push(2)  # This will print "Overflow"

print(s.pop())
print(s.stack)
