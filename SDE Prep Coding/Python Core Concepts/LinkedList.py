class Node:
    def __init__(self,value=None,next=None) -> None:
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insert(self):
        pass

    def delete(self):
        pass


n1=Node(3)
n2=Node(5)
n3=Node(6)
n4=Node(9)

LL=LinkedList()
LL.head=n1

#Instead of this Node Object can be Directly Assigned
# LL.head.next=n2
# LL.head.next.next=n3
# LL.head.next.next.next=n4 
n1.next=n2
n2.next=n3
n3.next=n4 #Ignoring n.next since by default the Next value is Initialised to None

print(n2.next.value)
