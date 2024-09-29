from node import Node

# def comp_1(node_1, node_2):
    
#     return node_1.key < node_2.key
def comp_1(node_1:Node, node_2:Node):
    return node_2.key1>node_1.key1

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    
    # def height(self, node):
    #     if not node:
    #         return 0
    #     return node.height
    def height_of_tree(self, node):
        if not node:
            return 0
        return node.height
    
    def leftrotate(self, root):
        node = root.right
        node1 = node.left
        node.left = root
        root.right = node1
        root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))
        node.height = 1 + max(self.height_of_tree(node.left), self.height_of_tree(node.right))
        return node

    def rightrotate(self, root):
        node = root.left
        node1 = node.right
        node.right = root
        root.left = node1
        root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))
        node.height = 1 + max(self.height_of_tree(node.left), self.height_of_tree(node.right))
        return node
    
    # def get_balance(self, node):
    #     if not node:
    #         return 0
    #     return self.height(node.left) - self.height(node.right)
    def diffbalance(self, node):
        if not node:
            return 0
        return self.height_of_tree(node.left) - self.height_of_tree(node.right)

    # def insert(self, root:Node, new:Node):
    #     if root is None:
    #         # new.ptr=my_bin

    #         return new
        
    #     if root.key1 >new.key1:
    #         root.left = self.insert(root.left, new)
    #         root.left.parent=root
    #     elif root.key1 <new.key1:
    #         root.right = self.insert(root.right, new)
    #         root.right.parent=root
    #     else:
    #         if new.key2 < root.key2:
    #             root.left = self.insert(root.left, new)
    #             root.left.parent=root
    #         else:
    #             root.right = self.insert(root.right, new)
    #             root.right.parent=root

    #     root.height = 1 + max(self.height(root.left), self.height(root.right))
    #     balance = self.get_balance(root)

    #     # Left Left Case
    #     if balance > 1 and new.key1<root.left.key1:
    #         return self.right_rotate(root)

    #     # Right Right Case
    #     if balance < -1 and root.right.key1<new.key1:
    #         return self.left_rotate(root)

    #     # Left Right Case
    #     if balance > 1 and new.key1<root.left.key1:
    #         root.left = self.left_rotate(root.left)
    #         return self.right_rotate(root)

    #     # Right Left Case
    #     if balance < -1 and new.key1<root.right.key1:
    #         root.right = self.right_rotate(root.right)
    #         return self.left_rotate(root)

    #     return root


    def insert(self, ele: Node, root):
        if root is None:
            self.size += 1
            return ele
        
        if self.comparator(root, ele):
            root.right = self.insert(ele, root.right)
        elif self.comparator(ele, root):
            root.left = self.insert(ele, root.left)
        else:
            if ele.key2 > root.key2:
                root.right = self.insert(ele, root.right)
            else:
                root.left = self.insert(ele, root.left)

        root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))
        balance = self.diffbalance(root)

        # RR
        if balance > 1 and (self.comparator(ele, root.left) or (ele.key1 == root.left.key1 and ele.key2 < root.left.key2)):
            return self.rightrotate(root)
        
        # LR
        if balance < -1 and (self.comparator(root.right, ele) or (ele.key1 == root.right.key1 and ele.key2 > root.right.key2)):
            return self.leftrotate(root)
        
        # LRR
        if balance > 1 and (self.comparator(root.left, ele) or (ele.key1 == root.left.key1 and ele.key2 > root.left.key2)):
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        
        # RLR
        if balance < -1 and (self.comparator(ele, root.right) or (ele.key1 == root.right.key1 and ele.key2 < root.right.key2)):
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)

        return root
    
    def min_value_node(self, node):
        if node==None:
            return 0
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def max_value_node(self, node):
        if node==None:
            return 0
        current = node
        while current.right is not None:
            current = current.right
        return current.key
    
    # def delete_node(self, root1,key, id):
        
    #     self.root = self.delete(self.root, key, id)
    # def delete(self, root:Node, key, id):
    #     if root is None:
    #         return root
    #     # Traverse the tree to find the node to delete
    #     if key < root.key1:
    #         root.left = self.delete(root.left, key, id)
    #     elif key > root.key1:
    #         root.right = self.delete(root.right, key, id)
    #     else:
    #         if(id>root.key2):
    #             root.right = self.delete(root.right, key, id)
    #         elif(id<root.key2):
    #             root.left = self.delete(root.left, key, id)
    #             # Node to be deleted found
    #         else:   
            
    #             if root.left is None or root.right is None:  # One child or no child
    #                 temp = root.left if root.left else root.right
    #                 if temp is None:  # No child case
    #                     if root.parent:  # Ensure parent is not None
    #                         if root.parent.left == root:
    #                             root.parent.left = None
    #                             root.parent=None
    #                         else:
    #                             root.parent.right = None
    #                             root.parent=None
    #                     root = None  # Set root to None
    #                 else:  # One child case
    #                     temp.parent = root.parent  # Update parent pointer
    #                     if root.parent:  # Connect parent to child
    #                         if root.parent.left == root:
    #                             root.parent.left = temp
    #                             root.parent=None
    #                         else:
    #                             root.parent.right = temp
    #                             root.parent=None
    #                     if root.left==temp:
    #                         root.left = None
    #                     else:
    #                         root.right=None
    #                     # root = temp   Replace root with child
    #             else:
    #                 # Node with two children
    #                 temp = self.min_value_node(root.right)  # Get inorder successor
    #                 root.key1 = temp.key1  # Replace root's key with successor's key
    #                 root.key2 = temp.key2  # Replace ID if necessary
    #                 root.ptr = temp.ptr
    #                 root.right = self.delete(root.right, temp.key1, temp.key2)  # Delete successor

    #     if root is None:
    #         return root
    #     # Update the height of the current node
    #     root.height = 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))

    #     # Check the balance of the current node and apply rotations if necessary
    #     balance = self.diffbalance(root)
    #     # Left Left Case
    #     if balance > 1 and self.diffbalance(root.left) >= 0:
    #         return self.rightrotate(root)

    #     # Left Right Case
    #     if balance > 1 and self.diffbalance(root.left) < 0:
    #         root.left = self.leftrotate(root.left)
    #         return self.rightrotate(root)

    #     # Right Right Case
    #     if balance < -1 and self.diffbalance(root.right) <= 0:
    #         return self.leftrotate(root)

    #     # Right Left Case
    #     if balance < -1 and self.diffbalance(root.right) > 0:
    #         root.right = self.rightrotate(root.right)
    #         return self.leftrotate(root)
    #     return root

    def _delete_node(self,node:Node,root:Node):
        if root==None:
            return root
        else:
            if self.comparator(node,root) or (node.key1==root.key1 and node.key2<root.key2):
                root.left=self._delete_node(node,root.left)
            elif self.comparator(root,node) or (node.key1==root.key1 and node.key2>root.key2):
                root.right=self._delete_node(node,root.right)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp=self.min_value_node(root.right)
                root.key1=temp.key1
                root.key2=temp.key2
                root.ptr=temp.ptr
                root.right=self._delete_node(temp,root.right)
            if root==None:
                return root
            root.height=1+max(self.height_of_tree(root.left),self.height_of_tree(root.right))
            balance=self.diffbalance(root)
            if balance > 1 and self.diffbalance(root.left) >= 0:
                return self.rightrotate(root)
            if balance > 1 and self.diffbalance(root.left) < 0:
                root.left = self.leftrotate(root.left)
                return self.rightrotate(root)
            if balance < -1 and self.diffbalance(root.right) <= 0:
                return self.leftrotate(root)
            if balance < -1 and self.diffbalance(root.right) > 0:
                root.right = self.rightrotate(root.right)
                return self.leftrotate(root)
            return root
    
    def search_id(self,root:Node,key):
        if root==None:
            # print('empty')
            return None
        if root.key1==key:
            # print('found')
            return root
        elif root.key1>key:
            return self.search_id(root.left,key)
        elif root.key1<key:
            return self.search_id(root.right,key)
    def search_id_part2(self,root:Node,key1,key2):
        if root==None:
            return None
        if root.key1==key1 and root.key2==key2:
            return root
        elif root.key1<key1 or (root.key1==key1 and root.key2<key2):
            return self.search_id_part2(root.right,key1,key2)
        elif root.key1>key1 or (root.key1==key1 and root.key2>key2):
            return self.search_id_part2(root.left,key1,key2)
    def insert_node_3(self,val1,val2,val3):
        # val1 is dominating
        node=Node(val1,val2)
        node.ptr=val3
        self.root=self.insert(node,self.root)
    def insert_node_2(self,val1,val2):
        # val1 is dominating
        node=Node(val1,val2)
        # print('in insert',node.key1,node.key2)
        self.root=self.insert(node,self.root)
    def in_order_traversal(self, root:Node,li:list):
        if not root:
            return
        self.in_order_traversal(root.left,li)
        li.append(root.key1)
        self.in_order_traversal(root.right,li)
        return
    

