import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def change(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)

number_of_nodes = random.randint(1, 10)
datas = random.sample(range(1, 100), number_of_nodes)

ll = linkedList()
for data in datas:
    ll.insert(data)

print(f"Initial linked list: {ll}")
data_to_delete = random.choice(datas)
ll.delete(data_to_delete)
print(f"Linked list after deleting {data_to_delete}: {ll}")

data_to_change = random.choice(datas)
new_data = random.randint(1, 100)
ll.change(data_to_change, new_data)
print(f"Linked list after changing {data_to_change} with {new_data}: {ll}")

data_to_search = random.randint(1, 100)
if ll.search(data_to_search):
    print(f"{data_to_search} is found in the linked list.")
else:
    print(f"{data_to_search} is not found in the linked list.")

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def change(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " <-> ".join(result)

dll = DoubleLinkedList()
for data in datas:
    dll.insert(data)
print(f"Initial double linked list: {dll}")