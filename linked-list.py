class Node:
    def __init__(self, value=None, next:object=None):
        self.value = value
        self.next = next

class SLinkedList:
    def __init__(self, head:Node=None):
        self.head = head

    def print_list(self):
        """
        Pirnt all elements in the linked list
        """
        # This has an O(n) time complexity because we have to traverse every item in the linked list
        # to print its value. (runs in linear time)
        
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

    def insert_in_front(self, value):
        """
        Insert a node with the specified "value" at the start of the linked list
        """
        #This probably has an O(1) or time complexity (runs in constant time)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """
        Appends a node with the specified "value" to the end of the liked list
        """
        # This action probably has an O(n) time complexity, because 
        # we would have to traverse all items in the linked list to find the last one.
        # (runs in linear time)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, value, after:Node):
        """Inserts a node with "value" after the "after" Node"""
        if not after:
            raise ValueError("The specified after node does not exist")
        new_node = Node(value)
        new_node.next = after.next
        after.next = new_node

    def delete(self, value):
        """Delete node with the specified "value" """
        # we need the value before the node we want to delete prev_node
        # compare all the node (curr_node) values to the deleting value
        # if the node is not what we're looking for, we set prev_node to curr_node and move on
        # if it is what we're looking for, we set prev_node.next = curr_node.next and set curr_node.next to None
        # that way, it does not point to anythin and nothing points to it and its effectively deleted
        prev_node = self.head
        if prev_node and prev_node.value == value:
            self.head == None
            return

        if not prev_node:
            raise ValueError(f'Node with value {value} does not extst.')

        while prev_node.next:
            curr_node = prev_node.next
            if curr_node.value == value:
                prev_node.next = curr_node.next
                curr_node.next = None
                return
                
            prev_node = curr_node
            curr_node = curr_node.next
        raise ValueError(f'Node with value {value} does not extst.')
        

list1 = SLinkedList(Node('First'))
n2 = Node('node 2')
list1.head.next = n2
list1.insert_in_front('inserted')
list1.append('End element')
list1.insert("yo I'm in NewYork", n2)
# list1.delete('sec')
list2 = SLinkedList(None)
list2.delete('value')
list1.print_list()