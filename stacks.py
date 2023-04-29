class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Add a new item to the end of the stack if the element does not already exist."""
        if value not in self.stack:
            self.stack.append(value)
            return True
        else:
            return False

    def peek(self):
        """Returns the last item in the stack."""
        return self.stack[-1]

    def pop(self):
        """Remove and return the last element in the stack."""
        if len(self.stack) <= 0:
            return None
        return self.stack.pop()

tech_stack = Stack()
tech_stack.push('Python')
tech_stack.push('JavaScript')
print(tech_stack.pop())
print(tech_stack.peek())