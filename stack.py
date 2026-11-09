class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
import random

n = random.randint(1, 10)
datas = random.sample(range(1, 100), n)

stack = Stack()
for data in datas:
    stack.push(data)

print(f"Initial stack: {stack}")

print(f"Stack size: {stack.size()}")

print(f"Top element: {stack.peek()}")

print(f"Popped element: {stack.pop()}")

print(f"Stack after popping: {stack}")