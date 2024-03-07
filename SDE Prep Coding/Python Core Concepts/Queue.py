#List Based Queue
class Queue:
    def __init__(self) -> None:
        self.queue=[]
    
    #Add an item to the Queue
    def enQueue(self,item):
        self.queue.append(item)
    
    #Returns the size of the Queue
    def sizeOfQueue(self):
        return len(self.queue)

    #Removes the First Item from the Queue
    def deQueue(self):
        First_Element=self.queue[0]
        self.queue=self.queue[1:]
        return First_Element
    
    #Returns if the Queue is Empty or Not
    def isEmpty(self):
        return len(self.queue) == 0

    def printQueue(self):
        return self.queue

#List Based Queue   
# Q=Queue()

# Q.enQueue(100)
# Q.enQueue(200)
# Q.enQueue(300)
# Q.enQueue(400)

# print(Q.printQueue())  
# print(Q.sizeOfQueue())
# print(Q.isEmpty())

# print(f'{Q.deQueue()} has been De-Queued')
# print(Q.printQueue()) 

class Queue:
    def __init__(self) -> None:
        self.enqueue_stack=[]
        self.dequeue_stack=[]
    
    def EnQueue(self,item):
        self.enqueue_stack.append(item)
    
    def DeQueue(self):
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                item=self.enqueue_stack.pop()
                self.dequeue_stack.append(item)
        if len(self.dequeue_stack) == 0:
            return None
        else:
            self.dequeue_stack.pop()

    #Returns if the Queue is Empty or Not
    def isEmpty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0
    
    def printQueue(self):
        print(self.enqueue_stack)
        print(self.dequeue_stack)

Q1=Queue()

# Q1.EnQueue(1)
# Q1.EnQueue(3)
# Q1.EnQueue(4)

# Q1.printQueue()

# Q1.DeQueue()
# Q1.printQueue()

#DeQueue (Double-ended Queue) -- Insertion and Deletion can happen at Two Ends of the Queue at faster manner
from collections import deque

DeQ= deque()
DeQ.append(100)
DeQ.appendleft(500)
DeQ.appendleft(2000)
DeQ.appendleft(6000)
DeQ.appendleft(7500)
print(DeQ)

# print(DeQ.count(100))  #Returns the No of occurences of the specified item in a queue

# DeQ.popleft()
# print(DeQ)

DeQ.popleft() #Removed the First Element in a Queue
print(DeQ)

DeQ.rotate(2)
print(DeQ)

DeQ.reverse()
print(DeQ)

DeQ.extend([8000,13000,19000])
print(DeQ)