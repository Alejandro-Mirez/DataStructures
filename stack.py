
class Stack:

    def __init__(self, values = []):
        self.values = values

    def is_empty(self):
        return len(self.values) == 0

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty. Can't return another value")
        last = self.values[len(self.values)-1]
        self.values.pop()
        return last