class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is Empty")
        else:
            return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("Stack is Empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print(self):
        print(" ".join(list(map(str, self.stack))))


stack = Stack()
for i in range(10):
    stack.push(i)

stack.push(10)
print(stack.peek())
stack.print()
