
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Stack:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def push(self,data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return
    
    def pop(self):
        if self.head is not None:
            poped_node = self.head
            self.head = self.head.next_node
            self.size -= 1
            return poped_node.data
        return "empty stack"

    def peek(self):
        if self.head is not None:
            return self.head.data
        return "empty stack"

    def printstack(self):
        if self.head is not None:
            self._data = []
            node = self.head
            while node:
                self._data.append(node.data)
                node = node.next_node
            print(self._data)
        else:
            print("empty stack")
    def stackSize(self):
        return self.size