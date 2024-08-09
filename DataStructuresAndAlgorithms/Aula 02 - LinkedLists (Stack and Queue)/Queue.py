#@Author: Prof. Andre Hochuli @data: 08/2022 @updated 08/2024

# Node class
class Node:

    
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
   
# Queue class
class Queue:
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
    
    def push(self,data):

        #First element
        if self.isEmpty():
            node = Node(data)
            self.head = node 
            self.tail = node            

        #Insert at Head
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
               

        self.length += 1

        return
    
    def pop(self):        
        
        if self.isEmpty():
            print("Nothing to remove")

        
        #In queue, we can only walk from head to position reach the tail. 
        #We cannot walk in the opposite direction (tail->head) since we did not have 'link'. 
        #So, to remove tail elements, we need to walk the whole list to re-link the tail to an element before it. 
        else:
            
            it = self.head
            i = 0 

            #Why length-2? To stop before the tail
            while(i<self.length-2): #or (it.next.next != None)                
                it = it.next
                i+=1

            node = it.next
            
            it.next=node.next
            self.tail = it
            
                
            del node
             
        self.length -= 1
            
    def print(self):

        if self.isEmpty():
            print("Nothing to print (Empty Stack)")
            return
        
        it = self.head
        
        while(it != None):
            print (it.data)            
            it = it.next

      
        
llist = Queue()

llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)
llist.push(70)
print('---------')
llist.print()
print('--Removing from tail ---')
llist.pop()
llist.print()
print('--Removing from tail ---')
llist.pop()
llist.print()
print('--Removing from tail ---')
llist.pop()
llist.print()
print('--Removing from tail ---')
llist.pop()
llist.print()







