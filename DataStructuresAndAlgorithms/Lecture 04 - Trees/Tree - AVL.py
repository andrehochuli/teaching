class Node:
    def __init__(self,data): 
        self.data = data  # Assign data
        self.left = None  # Initialize as None
        self.right = None  # Initialize as None
        
        
class AVLTree:
    
    # Init Class
    def __init__(self,data): 
        self.root = Node(data)
        self.height = 1
    def push(self,data):        

        if self.root is None:
            print("Root")
            self.root = AVLTree(data)

        if data > self.root.data:            
            if self.root.right is None:                
                self.root.right = AVLTree(data)
            else:
                self.root.right.push(data)
                
        else:            
            if self.root.left is None:                
                self.root.left = AVLTree(data)
            else:
                self.root.left.push(data)

        self.height = 1 + max(self.getHeight(self.root.left),
                                   self.getHeight(self.root.right))

        
        #balance factor
        balanceFactor = self.getBalance(self.root)
        if balanceFactor > 1:
            if data < self.root.left.data:
                return self.rightRotate(self.root)
            else:
                self.root.left = self.leftRotate(self.root.left)
                return self.rightRotate(self.root)

        if balanceFactor < -1:
            if data > self.root.right.data:
                return self.leftRotate(self.root)
            else:
                self.root.right = self.rightRotate(self.root.right)
                return self.leftRotate(self.root)
        return

    # Get the height of the node
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factore of the node
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    # Function to perform left rotation
    def leftRotate(self, node):
        y = node.right
        T2 = y.left
        y.left = z
        node.right = T2
        node.height = 1 + max(self.getHeight(node.left),
                           self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, node):
        y = node.left
        T3 = y.right
        y.right = z
        node.left = T3
        node.height = 1 + max(self.getHeight(node.left),
                           self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    
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
    
        
tree_root = AVLTree(10)
tree_root.push(15)
tree_root.push(5)
tree_root.push(25)
tree_root.push(30)


print('#### Pre-Order ####')
tree_root.walk_preorder()





                

        
            
            

                        
