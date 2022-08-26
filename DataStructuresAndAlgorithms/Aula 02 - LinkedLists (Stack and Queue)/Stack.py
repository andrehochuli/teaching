#@Author: Prof. Andre Hochuli @data: 08/2022

# Node class
class Node:
   
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
   
# Stack class
class Stack:
    length = 0
    # Function to initialize the Stack
    def __init__(self): 
        self.head = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        
    def size(self):
        return self.length

    #Insert at Head
    def push(self,data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

        self.length += 1

    #Remove from Head
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop")
        else:
            node = self.head
            self.head = self.head.next
            print("removed ", node.data)
            del node

        self.length -= 1
            
    def print(self):

        if self.isEmpty():
            print("Empty Stack")
            return
        
        it = self.head
        
        while(it != None):            
            print (it.data)
            it = it.next
        
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("----------")
stack.print()
print("----------")

print("----------")
print("Removing from Head")
stack.pop()
print("----------")
stack.print()
print("----------")

print("Removing from Head")
stack.pop()
print("----------")
stack.print()
print("----------")

print("Removing from Head")
print("----------")
stack.pop()
print("----------")
stack.print()
print("----------")

print("Removing from Head")
stack.pop()
print("----------")
stack.print()

print("Removing from Head")
stack.pop()
print("----------")
stack.print()
print("----------")


