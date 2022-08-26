class Node:
    def __init__(self,data): 
        self.data = data  # Assign data
        self.left = None  # Initialize as None
        self.right = None  # Initialize as None
        
class Binary_Tree:
    
    # Init Class
    def __init__(self,data): 
        self.root = Node(data)

    def push(self,data):        

        if self.root is None:
            print("Root")
            self.root = Binary_Tree(data)

        if data > self.root.data:            
            if self.root.right is None:
                print("Add Right")
                self.root.right = Binary_Tree(data)
            else:
                self.root.right.push(data)
                
        else:            
            if self.root.left is None:
                print("Add Left")
                self.root.left = Binary_Tree(data)
            else:
                self.root.left.push(data)

        return

    def walk_preorder(self):
        
        print(self.root.data)
        
        if self.root.left is not None:
            self.root.left.walk_preorder()
        
        if self.root.right is not None:
            self.root.right.walk_preorder()

    def walk_inorder(self):
        
        if self.root.left is not None:
            self.root.left.walk_inorder()

        print(self.root.data)
        
        if self.root.right is not None:
            self.root.right.walk_inorder()
    

    def walk_postorder(self):
        
        if self.root.left is not None:
            self.root.left.walk_postorder()
        
        
        if self.root.right is not None:
            self.root.right.walk_postorder()

        print(self.root.data)
    
        
tree_root = Binary_Tree(10)
tree_root.push(15)
tree_root.push(5)
tree_root.push(12)
tree_root.push(17)
tree_root.push(8)
tree_root.push(4)


print('#### Pre-Order ####')
tree_root.walk_preorder()

print('#### In-Inorder ####')
tree_root.walk_inorder()

print('#### Post-order ####')
tree_root.walk_postorder()



                

        
            
            

                        
