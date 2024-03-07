from ctypes import sizeof


class Node:
    def __init__(self,val) -> None:
        self.val=val 
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.size=0
        
    def get(self, Index : int):
        if Index < 0 or Index >= self.size :
            return -1
        
        curr = self.head
        while Index != 0:
            curr = curr.next
            Index = Index - 1
            
        return curr.val

    def addElementatHead(self,val :int):
        NN=Node(val)
        
        if self.head == None:
            self.head=NN
            self.tail=NN
           
        else:
            NN.next=self.head
            self.head.prev=NN
            NN.prev=None
            self.head=NN
            
        self.size+=1
    
    def addElementatTail(self,val :int):
        NN=Node(val)
        
        if self.tail == None:
            self.head=NN
            self.tail=NN
        else:
            self.tail.next=NN
            NN.next=None
            NN.prev=self.tail
            self.tail=NN
            
        self.size+=1
    
    def addAtIndex(self,Index,val):
        if Index < 0 or Index >= self.size:
            return -1
        elif Index ==0:
            self.addElementatHead(val)
        elif Index == self.size:
            self.addElementatTail(val)
        else:
            NN=Node(val)
            cur = self.head
            while Index-1 !=0:
                cur = cur.next
                Index = Index-1
            NN.next=cur.next
            NN.prev=cur
            
            cur.next=NN.prev
            cur.next.prev=NN
            
            self.size+=1
    
    def deleteElementatHead(self):
        if self.size == 1:
            self.head=None
            
        self.head = self.head.next #Moving Head to Next Node
        self.head.prev=None #Removing the connection to Previous Head
        self.size-=1
        
    def deleteElementatTail(self):
        if self.size == 1:
            self.tail=None
            
        self.tail = self.tail.prev
        self.tail.next=None
        self.size-=1
        
             
    def deleteElementatIndex(self,Index):
        if Index < 0 or Index > self.size:
            return -1
        elif Index == 0:
            self.deleteElementatHead()
        elif Index == self.size:
            self.deleteElementatTail()
        else:
            cur=self.head
            while Index-1 !=0:
                cur = cur.next
                Index = Index-1
                
            cur.next=cur.next.next
            cur.next.prev=cur
            
            
        
n1=Node(4)
n2=Node(5)
n3=Node(7)
n4=Node(9)
n5=Node(15)

#Head --> N1 --> N2 --> N3
LL=LinkedList()
LL.addElementatHead(5)
LL.addElementatTail(26)
# print(LL.head.val)
# print(LL.tail.val)
# print(LL.size)
# LL.deleteElementatHead()
# print(LL.size)
LL.deleteElementatTail()
print(LL.size)
print(LL.head.val)
print(LL.tail.val)
# print(LL.head.next)
# LL.deleteElementatTail()

# LL.head=n1
# n1.next=n2
# n1.prev=None

# n2.prev=n1
# n2.next=n3

# n3.next=n4
# n3.prev=n2

# n4.next=n5
# n4.prev=n3

# LL.tail=n5
# n5.next=None
# n5.prev=n4

# print(LL.tail.val)
