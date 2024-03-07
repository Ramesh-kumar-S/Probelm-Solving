import sys
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
        """Traveses over the Linked List and returns the total number of nodes present on it

            Time Complexeity - O(n) - Since we need to visit every node to calculate total size"""
        size=0
        if self.head is None :
            return size
        
        Current = self.head
        while Current is not None :
            print(Current.get_data())
            Current = Current.get_next()
            size+=1
        return  size
    
    def search(self, key):
        """Traveses over the Linked List and returns whether the Key is present on it

            Time Complexeity - O(n) - Since we need to visit every node to check the Key in a List"""
        if self.head is None :
            return "Oops!! Linked List seems to be empty"
        
        Current = self.head
        while Current is not None:
            
            if Current.get_data() == key:
                print("Yayy!! Key Found")
                return  True 
            else:
                Current = Current.get_next()
                
        print("Oops!! Key Not Found")
        return False 
                
    
    def add_front(self,new_data):
        temp = DoublyLinkedList(new_data)
        temp.set_next(self.head)
        self.head = temp
    
    def remove(self, data):
        
        #Edge Case 1 : Return False if LinkedList is Empty
        if self.is_empty():
            return "Linked List is Empty, No items to be Removed"
        
        #Edge Case 2 : Return False if Key Not Found in LinkedList
        Previous =None
        if not self.search(data):
            return  "Oops!! Key Not found, No data to be removed from the List"
        else:
            Current = self.head
            while Current is not  None:
                if Current.get_data() == data:
                    Previous = Current
                    Current = Current.get_next()
                    Previous.set_next(Current.get_next())
                    self.head = Previous
                    return  "Key Found and Removed"
                
        

#Create Linked List Object
L=LinkedList()
#print(L.remove(44))   ## Tested the Remove Edge Case 1 by Removing the Key on a List which is already Empty.

SDE1=DoublyLinkedList("Ramesh SDE-I Cisco")
SDE2=DoublyLinkedList("Ramesh SDE-III Google")
SDE3=DoublyLinkedList("Ramesh Senior SDE Microsoft")

L.add_front("Ramesh SDE-I Cisco")
L.add_front("Ramesh SDE-III Google")
L.add_front("Ramesh Senior SDE Microsoft")

# L.remove(25)  ## Tested the Remove Edge Case 2 by trying to remove the key which doesn't event exist on a List.

print(L.size())
# print(L.search("Ramesh SDE-I Cisco"))
SDE1.set_next(SDE2) #Connecting First node to Second Node
SDE2.set_next(SDE3) #Connecting Second node to Third Node

print(L.remove("Ramesh SDE-I Cisco"))
print(L.size())