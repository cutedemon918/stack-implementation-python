class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, item):
        if len(self.stack) >= self.capacity:
            print("Stack Overflow!")
        else:
            self.stack.append(item)
            print(item, "pushed into stack.")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow!")
        else:
            item = self.stack.pop()
            print(item, "popped from stack.")

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack:", self.stack)


# Create stack
capacity = int(input("Enter stack capacity: "))
s = Stack(capacity)

# Menu
while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to push: "))
        s.push(item)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")