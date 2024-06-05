class Stack:
    def __init__(self, items=None, limit=None):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, item):
        if item in self.items:
            return len(self.items) - self.items.index(item) - 1
        else:
            return -1