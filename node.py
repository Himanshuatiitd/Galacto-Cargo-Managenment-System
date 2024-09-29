# from avl import AVLTree
class Node:
    def __init__(self,key,id):
        # self.id=id
        # self.key=key
        # self.left=None
        # self.right=None
        # self.height=1
        # self.key = key
        # self.id = id
        self.key1=key
        self.key2=id
        self.key3=None
        
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at leaf
        self.ptr=None
        # self.avlt=None
        # self.av=AVLTree()

        # note:- here key is val1 and id is val2 

        
        
    
        
    def update_key(self,new_key):
        self.key=new_key
        
    def update_left(self,left_child):
        self.left=left_child
        
    def update_right(self,right_child):
        self.right=right_child
        
    def update_height(self,h):
        self.height=h
        
    def get_id(self):
        return self.id
    
    def get_key(self):
        return self.key
    
    
        
        
    
    