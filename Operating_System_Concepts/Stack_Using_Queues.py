from collections import deque

"""
Stack - LIFO

Queue - FIFO

"""
class StackUsingQueues:
    def __init__(self) -> None:
        self.queue1 = deque()
        self.queue2 = deque()
    
    def append(self, data):
        if not self.queue1:
            self.queue1.append(data)
        else:
            self.queue2.append(data)
    
    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        
        if self.queue2:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            return self.queue1.popleft()
        
    def top(self):
        result = None
        if self.queue1:
            while self.queue1:
                result = self.queue1.popleft()
                self.queue2.append(result)
        else:
            while self.queue2:
                result = self.queue2.popleft()
                self.queue1.append(result)
        return result

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


class StackUsingQueues:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int):
        self.queue.append(x)
        # Rotate the queue to move the new element to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
    """
    Remove Last Inserted element as First Element
    
    Remove LIFO Element using FIFO
    """
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

SQ = StackUsingQueues()