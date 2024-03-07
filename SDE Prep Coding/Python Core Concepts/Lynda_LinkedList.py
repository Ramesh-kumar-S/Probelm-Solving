class DoublyLinkedList:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
    def __repr__(self) -> str:
        return f'Current Role : {self.data}'
        
    def get_data(self):
        """ Returns  the current data on the Node - self.data """
        return self.data
    
    def set_data(self, new_data):
        """ Replaces the Existing self.data with new_data"""
        self.data = new_data
    
    def get_next(self):
        """ Returns the Next pointer of the Node"""
        return self.next
    
    def get_previous(self):
        """ Returns the previous pointer of the specific Node"""
        return self.prev
    
    def set_previous(self, new_prev):
        """ Replaces/Sets New Previous pointer"""
        self.prev = new_prev
    
    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    
    def __repr__(self) -> str:
        pass
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        pass
    
    def search(self, key):
        pass
    
    def add_front(self,new_data):
        temp = DoublyLinkedList(new_data)
        temp.set_next(self.head)
        self.head = temp
    
    def remove(self, data):
        pass

#Creating First Node and setting and getting data from it
Node1 = DoublyLinkedList("Ramesh - Software Engineer (Google)")
# print(Node1)
# print(Node1.get_data())

## Modifying the existing data on a Node 1
Node1.set_data("Ramesh - Senior Software Engineer (Microsoft)")
# print(Node1.get_data())
# print(Node1)

#Lets create an another node and attach it to first node
Node2 = DoublyLinkedList("Ramesh - Principle Software Engineer(Microsoft)")
Node1.set_next(Node2)

#Printing the Node1 Next pointer
# print(Node1.get_next())
# print(Node1.next.get_data())

#Lets create a circular Linked List First Node points to Second Node and Vice Versa
# Node1.set_previous(Node2)
# print(f'Getting Previous of Node1 -- {Node1.get_previous()}')

Node2.set_previous(Node1)
print(Node1.get_data())
print(Node1.get_next())
print(Node2.get_previous())


#Third Node and Append it to the Front
List = LinkedList()
List.head = Node1
print(List.head)
List.add_front("Ramesh - Software Engineer - Cisco")

# Node1.set_previous(List)

