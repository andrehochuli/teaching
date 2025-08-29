from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # subárvore esquerda (AVLTree)
        self.right = None  # subárvore direita (AVLTree)
        self.height = 1    # altura inicial

class AVLTree:
    def __init__(self, data):
        self.root = Node(data)

    def push(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            if node.left is None:
                node.left = AVLTree(data)
            else:
                node.left.root = self._insert(node.left.root, data)
        else:
            if node.right is None:
                node.right = AVLTree(data)
            else:
                node.right.root = self._insert(node.right.root, data)

        # Atualiza altura
        left_height = node.left.root.height if node.left else 0
        right_height = node.right.root.height if node.right else 0
        node.height = 1 + max(left_height, right_height)


        balance = left_height - right_height

        # Rotação Left-Left
        if balance > 1 and data < node.left.root.data:
            return self._right_rotate(node)

        # Rotação Right-Right
        if balance < -1 and data > node.right.root.data:
            return self._left_rotate(node)

        # Rotação Left-Right
        if balance > 1 and data > node.left.root.data:
            node.left.root = self._left_rotate(node.left.root)
            return self._right_rotate(node)

        # Rotação Right-Left
        if balance < -1 and data < node.right.root.data:
            node.right.root = self._right_rotate(node.right.root)
            return self._left_rotate(node)

        return node

    # Rotação à esquerda
    def _left_rotate(self, z):
        y = z.right.root
        T2 = y.left

        y.left = AVLTree(z.data)
        y.left.root.left = z.left
        y.left.root.right = T2

        # Atualiza alturas
        z_left_height = z.left.root.height if z.left else 0
        z_right_height = T2.root.height if T2 else 0
        y.left.root.height = 1 + max(z_left_height, z_right_height)

        y.height = 1 + max(y.left.root.height if y.left else 0,
                           y.right.root.height if y.right else 0)
        return y

    # Rotação à direita
    def _right_rotate(self, z):
        y = z.left.root
        T3 = y.right

        y.right = AVLTree(z.data)
        y.right.root.left = T3
        y.right.root.right = z.right

        # Atualiza alturas
        z_left_height = T3.root.height if T3 else 0
        z_right_height = z.right.root.height if z.right else 0
        y.right.root.height = 1 + max(z_left_height, z_right_height)

        y.height = 1 + max(y.left.root.height if y.left else 0,
                           y.right.root.height if y.right else 0)
        return y

    # ====== Percursos ======
    def walk_preorder(self):
        print(self.root.data)
        if self.root.left:
            self.root.left.walk_preorder()
        if self.root.right:
            self.root.right.walk_preorder()

    def walk_inorder(self):
        if self.root.left:
            self.root.left.walk_inorder()
        print(self.root.data)
        if self.root.right:
            self.root.right.walk_inorder()

    def walk_postorder(self):
        if self.root.left:
            self.root.left.walk_postorder()
        if self.root.right:
            self.root.right.walk_postorder()
        print(self.root.data)

    def walk_levelorder(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left:
                queue.append(node.left.root)
            if node.right:
                queue.append(node.right.root)

# ======= TESTE =======
tree_root = AVLTree(10)
tree_root.push(15)
tree_root.push(5)
tree_root.push(12)
tree_root.push(17)
tree_root.push(8)
tree_root.push(4)

print('#### Pre-Order ####')
tree_root.walk_preorder()

print('#### In-Order ####')
tree_root.walk_inorder()

print('#### Post-Order ####')
tree_root.walk_postorder()

print('#### Level-Order (BFS) ####')
tree_root.walk_levelorder()
