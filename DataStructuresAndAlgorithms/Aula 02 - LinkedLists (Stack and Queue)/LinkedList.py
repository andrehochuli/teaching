#@Author: Prof. Andre Hochuli @data: 08/2022

# Node class
class Node:
   
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
   
# Linked List class
class LinkedList:
    length = 0
    # Init Class
    def __init__(self): 
        self.head = None
        self.tail = None

    def isEmpty(self):
        if self.head == None:
            return True
    
    def size(self):
        return self.length
    
    def push(self,data,pos=-1):

        if pos > self.length:
            print("Cannot insert in %d. length == %d" % (pos,self.length))
            return

        #First element
        if self.isEmpty():
            node = Node(data)
            self.head = node 
            self.tail = node

        #Insert at Tail
        elif(pos == -1): 
            node = Node(data)
            self.tail.next = node
            self.tail = node

        #Insert at Head
        elif(pos == 0):
            node = Node(data)
            node.next = self.head
            self.head = node

        #Insert at any position    
        elif pos <= self.length: #Sanity check 
            it = self.head
            i = 1 
            while(i<pos):
                it = it.next
                i+=1
                
            temp = it.next
            node = Node(data)
            node.next = temp
            it.next = node

                        
        self.length += 1

        return
    
    def pop(self,pos=0):

        #Last postion index
        if pos == -1:
            pos = self.length-1
        
        if self.isEmpty():
            print("Nothing to remove")

        #Insert at Head
        elif pos==0:             
            node = self.head
            self.head = self.head.next
            del node

        #In a single linked list, we can only walk from head to position reach the tail. 
        #We cannot walk in the opposite direction (tail->head) since we did not have 'link'. 
        #So, to remove tail elements, we need to walk the whole list to re-link the tail to an element before it. 
        else:
            it = self.head
            i = 1 

            while(i<pos):                
                it = it.next
                i+=1

            node = it.next
            it.next=it.next.next
            del node

            if pos == self.length -1:
                self.tail = it
                self.tail.next = None
                
        self.length -= 1
            
    def print(self):
        if self.isEmpty():
            print("Empty Stack")
            return
        
        it = self.head
        
        while(it != None):
            print (it.data)
            it = it.next

       
        
llist = LinkedList()

llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)
llist.push(70)

llist.print()
print('--Removing from tail ---')
llist.pop(-1)
llist.print()
print('Removing from tail')
llist.pop(-1)
llist.print()
print('Removing from head')
llist.pop(0)
llist.print()
print('Removing pos 2: [0,1,(2)]')
llist.pop(2)
llist.print()







