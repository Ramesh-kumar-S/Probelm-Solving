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
    def __init__(self, head=None) -> None:
        self.head = head
        self.count = 0
    
    def get_count(self):
        return self.count

    def insert(self, value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head = new_node
        self.count += 1
    
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.getData() == value:
                print(f'Node found : {temp.getData()}')
                break
            temp = temp.getNext()
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(f'Node : {temp.getData()}')
            temp = temp.getNext()
    
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
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.printList()

# # exercise the list
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(13))
# print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.delete(3)
# print("Item count: ", itemlist.get_count())
# print("Finding item: ", itemlist.find(38))
itemlist.printList()



