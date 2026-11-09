class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")

    def __str__(self):
        return str(self.items)

    def size(self):
        return len(self.items)

import random
n = random.randint(1, 10)
datas = random.sample(range(1, 100), n)

queue = Queue()
for data in datas:
    queue.enqueue(data)
print(f"Initial queue: {queue}")
print(f"Queue size: {queue.size()}")
print(f"Front element: {queue.peek()}")
print(f"Dequeued element: {queue.dequeue()}")
print(f"Queue after dequeuing: {queue}")

