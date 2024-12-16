class QueueUsingStack:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    """
    Remove First Inserted element as a Last Element
    
    Remove FIFO Element using LIFO
    """

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def isEmpty(self):
        return not self.stack1 and not self.stack2
