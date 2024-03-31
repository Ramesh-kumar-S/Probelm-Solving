class MyQueue:

    def __init__(self):
        self.Queue = []

    def push(self, x: int) -> None:
        self.Queue.append(x)

    def pop(self) -> int:
        self.Queue.pop(0)
        
    def peek(self) -> int:
        print(self.Queue[0])
        # print(list(reversed(self.Queue))[-1])

    def empty(self) -> bool:
        return len(self.Queue) == 0

    def print(self) -> None:
        print(self.Queue)
        
# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.pop()
obj.empty()
# obj.push(25)
obj.print()
obj.peek()
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

