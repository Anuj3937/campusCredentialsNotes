class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if self.top == None :
            print("stack is empty")
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top=new_node 
    def pop (self):
        def pop(self):
         if self.isEmpty():
            raise IndexError("Pop from empty stack")
         popped = self.top.data
         self.top = self.top.next
         return popped

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Stack (top to bottom):", elements)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()        
    print(stack.pop())     
    print(stack.peek())    
    stack.display()        