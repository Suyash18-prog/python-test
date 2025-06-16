#  Create a stack class using a list and implement push(), pop(), and peek() methods.

class Stack:
    def __init__(self,stack):
        self.stack=stack

    def push(self,element):
        self.stack.append(element)
        print(f"{element} has been pushed to your stack")

    def pop(self):
        element =self.stack.pop() 
        print(f"{element} has been poped from your stack")

    def peek(self):
        print(f"peek of stack is {self.stack[-1]}")


stack = Stack([])
stack.push(5)
stack.push(2)
stack.peek()