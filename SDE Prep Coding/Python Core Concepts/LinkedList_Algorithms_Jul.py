# Linked List
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
    def getNext(self):
        return self.next

    def setNext(self, Next):
        self.next = Next
    
    def getData(self):
        return self.value

    def setData(self, value):
        self.value = value

class LinkedList(object):
    """
    LinkedList Class
        - Insert Element at End
        - Print the List
        - Search an Item in List
        - Insert at Specific Position
        - Delete at Specific Position
        - Delete Head/Tail
        - Get Mid Point of Element

    LinkedList is an Meta-data about the Nodes
    """
    def __init__(self, head=None) -> None:
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    def insert(self, value):
        """Inserts an Element at the End

        If the List is empty, New node will be added and marked as head

        Args:
            value (Node):   Node Object
        """
        #If the LinkedList is Empty, Add a Element and Make it as a Head
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.count+=1
            return
        
        #If Not add it to the End of the Linked List
        current = self.head
        while current.getNext():
            current = current.getNext()
        current.setNext(new_node)
        self.count+=1
        
        # new_node.setNext(self.head)
        # self.head = new_node
        # self.count += 1
    
    def getMidPointofList(self):
        """
        Approach 1 : Using getcount()//2 and finding the Mid Point
        
        Approach 2 : Fast & Slow Pointers
        """
        if self.head is None:
            print(f'List is Empty')
            return
        """
        Approach 1 - Using Median Value
        """
        # count = self.get_count()//2
        # current = self.head
        # while count > 0 and current:
        #     current = current.getNext()
        #     count-=1
        # print(current.getData())
        
        """
        Approach 2 - Using Fast and Slow Pointer
        """
        fast, slow = self.head, self.head
        
        while fast and fast.next:
            slow = slow.getNext()
            fast = fast.getNext().getNext()
        print(slow.getData())
    
    def insertElementAtPos(self, position, value):
        """
        Insert elements at specified position
        
        if position == Pos:
            Node.next = Current.next
            Current.next = Node
        Current = Current.next
        """        
        new_node = Node(value)
        Pos=0
        Current = self.head
        while Current:
            Pos+=1
            if Pos == position:
                new_node.next = Current.next
                Current.next = new_node
            Current = Current.next
    
    def insertElementAtHead(self, value):
        """
        Inserts Element at the Head
        """   
        new_node = Node(value)
        new_node.next(self.head)  
        self.head = new_node
          
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.getData() == value:
                print(f'Node found : {temp.getData()}')
                break
            temp = temp.getNext()
    
    def printList(self):
        Output = []
        temp = self.head
        while temp is not None:
            Output.append(str(temp.getData()))
            print(f'Node : {temp.getData()}')
            temp = temp.getNext()
        print(" -> ".join(Output))
        print(f'Count of Hierarchy : {self.get_count()}')
    
    def printListinReverse(self, Node):
        # Current = self.head
        if Node:
           
            self.printListinReverse(Node.getNext())
            print(Node.getData(), end=" ")
        else:
            return
    
    def delete(self, index):
        temp = self.head
        if index > self.count -1:
            raise ValueError("Invalid Index")

        if self.head == None:
            #Logic 1
            # NxtNode = temp.getNext()
            # temp.setNext(None)
            # self.head = NxtNode
           
            #Logic 2
            self.head = self.head.getNext()
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < index - 1:
                node = node.getNext()
                tempIdx+=1
            node.setNext(node.getNext().getNext())
            self.count-=1
            
class RevLinkedList(LinkedList):
    def __init__(self, head=None) -> None:
        super().__init__(head)
    
    def insert(self, value):
        return super().insert(value)
    
             
# create a linked list and insert some items
#Try Insertion at the End
itemlist = LinkedList()
itemlist.insert("Ramesh Kumar Sekar")
itemlist.insert("Jai Anand")
itemlist.insert("Bala")
itemlist.insert("Wink Ko")
itemlist.insert("Salman Hassan")
itemlist.insert("Jeremy Foster")
itemlist.insert("Chuck Robbins")

itemlist.printList()
itemlist.getMidPointofList()
# itemlist.insertElementAtHead(1, "Sabari Girish")
itemlist.printListinReverse(itemlist.head)


# # exercise the list
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(78))

# delete an item
# itemlist.delete(3)
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(38))
# itemlist.printList()



