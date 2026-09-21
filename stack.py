class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow")
        else:
            self.stack.append(item)
            print(item, "pushed into stack")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            item = self.stack.pop()
            print(item, "popped from stack")

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack:", self.stack)


# Create a stack
s = Stack(5)

# Perform stack operations
s.push(10)
s.push(20)
s.push(30)

s.display()

s.pop()

s.display()