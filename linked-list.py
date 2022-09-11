class Node:
    def __init__(self, value=None, next:object=None):
        self.value = value
        self.next = next

class SLinkedList:
    def __init__(self, head:Node):
        self.head = head

list1 = SLinkedList(Node('First'))

print(list1.head.value)