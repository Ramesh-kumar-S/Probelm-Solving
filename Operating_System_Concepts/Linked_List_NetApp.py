import random
import sys

sys.setrecursionlimit(3000)


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def search_v1(self, data):
        if self.data == data:
            return True

        if self.next:
            return self.next.search_v1(data)
        return False


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get_middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def recursive_search(self, data):
        return self.head.search_v1(data)

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        if self.head.data > data:
            old_head = self.head
            new_node.next = old_head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.data > data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        print("Ramesh Kumar Sekar", end=" - ")
        print(" -> ".join(output))

    def remove_duplicates(self):
        current = self.head
        if not current:
            return

        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def merge_two_lists(self, l1, l2):
        dummy = Node(0)
        current = dummy
        
        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        Res = dummy.next
        Output = []
        while Res:
            Output.append(str(Res.data))
            Res = Res.next
        print("->".join(Output))

class CircularLinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.head.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def print(self):
        if not self.head:
            return

        output = []
        current = self.head
        while current.next != self.head:
            output.append(str(current.data))
            current = current.next

        output.append(str(self.tail.data))

        print("Circular Linked List", end=" - ")
        print(" -> ".join(output))


class DNode(Node):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.prev = None


class DoublyLinkedList(LinkedList):
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        # current = self.head
        # while current.next:
        #     current = current.next
        # current.next = new_node
        # new_node.prev = current

    # Additonal Note : Reversing can be performed using tail too.
    def reverse(self):
        """
        Double Traversing Approach
        
        - Traverse the whole list using next pointer
        - again traverse to the start using prev pointer
        """
        # current = self.head
        # while current.next:
        #     current = current.next

        # while current and current.prev:
        #     print(f'{str(current.prev.data)}', end="->")            
        #     current = current.prev
        
        """
        Reverse the Pointer
        """
        current = self.head
        prev = None
        self.tail = self.head  # Update tail to the current head

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        self.head = prev  # Update head to the new front of the list
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

N1 = Node(1)
N1.next = Node(2)
N1.next.next = Node(3)


Companies = ["Google", "Cisco", "Nutanix", "NetApp", "MapleLabs", "Xoriant"]
random.shuffle(Companies)

# LL = LinkedList()
# for company in Companies:
#     LL.append(company)

# LL.print()
# print(f'Middle of the List : {LL.get_middle()}')
# LL.delete("Xoriant")
# LL.print()

L1 = LinkedList()
for i in range(1,10):
    L1.append(i)

L1.print()

L2 = LinkedList()
for i in range(10,100, 10):
    L2.append(i)

L2.print()
L1.merge_two_lists(L1.head, L2.head)

# L1.insert(33)
# L1.insert(0)
# L1.insert(-1)
# L1.print()
# L1.remove_duplicates()
# L1.print()
# print(L1.recursive_search(5))

# Circular Linked List
# CL = CircularLinkedList()
# for i in range(6):
#     CL.append(i)
# CL.print()

# DLL = DoublyLinkedList()
# for i in range(10):
#     DLL.append(i)
# DLL.print()
# DLL.reverse()
# Recursive search Limit
# print(sys.getrecursionlimit())


