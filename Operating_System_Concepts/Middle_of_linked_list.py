class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    
    def find_middle(self):
        current = self.head
        if not current:
            return None
        
        fast_pointer = self.head
        slow_pointer = self.head
        
        while fast_pointer  and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer
    
    def reverse_list(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        #Print it 
        while prev:
            print(prev.value, end=" -> ")
            prev = prev.next
        print("None")
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        return

# Example usage
linked_list = LinkedList()
values = [1, 2, 3, 4, 5]
for value in values:
    linked_list.insert(value)

print("Original Linked List:")
linked_list.print_list()

middle_node = linked_list.find_middle()
if middle_node:
    print(f"\nThe middle node value is: {middle_node.value}")
else:
    print("The linked list is empty.")

linked_list.reverse_list()
    
