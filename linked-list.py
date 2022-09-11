class Node:
    def __init__(self, value=None, next:object=None):
        self.value = value
        self.next = next

class SLinkedList:
    def __init__(self, head:Node=None):
        self.head = head

    def print_list(self):
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

list1 = SLinkedList(Node('First'))
n2 = Node('node 2')
list1.head.next = n2

list1.print_list()