from collections import deque 

class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None


class BTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node=Node(val)
        if self.root is None:
            self.root=new_node
            return
        queue=deque([self.root])
        while queue:
            current=queue.popleft()
            if current.left is None:
                current.left=new_node
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right=new_node
                return
            else:
                queue.append(current.right)
                    

