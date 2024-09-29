from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_id=AVLTree()
        self.bin_capacity=AVLTree()
        self.object_id=AVLTree()
    def minimum_val_node(self,root)->Node:
        curr=root
        while curr.left!=None:
            curr=curr.left
        return curr
    def successor(self,node:Node):
        if node.right:
            return self.minimum_val_node(node.right)
        successor = None
        ancestor = self.bin_capacity.root
        while ancestor != node:
            if node.key1 < ancestor.key1:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor
    def least_node(self,node:Node,size):
        curr=node
        while curr!=None:
            if curr.left==None and curr.key1>size:
                return curr
            elif curr.right==None and curr.key1<size:
                return self.successor(curr)
            if curr.key1==size:
                return curr
            elif curr.key1>size:
                curr=curr.left
            else:
                curr=curr.right
    def search(self,node:Node,value):
        if node.key1==value:
            return node
        elif node.key1<value:
            return self.search(node.right,value)
        else:
            return self.search(node.left,value)
    def compact_min(self,obj:Object,node:Node):
        node1=self.bin_capacity.root
        curr=node1
        while curr.right!=None:
            curr=curr.right
        if curr.key1<obj.size:
            raise NoBinFoundException
        val=self.least_node(self.bin_capacity.root,obj.size).key1
        node=self.search(self.bin_capacity.root,val)
        ans=node
        while node is not None:
            if node.key1==val:
                ans=node
                node=node.left
            elif node.key1<val:
                node=node.right
        node=ans
        new_size=node.key1-obj.size
        bin_id=node.key2
        new_node=Node(new_size,bin_id)
        new_node.ptr=node.ptr
        self.bin_capacity._delete_node(node,self.bin_capacity.root)
        # print(new_node.key1,new_node.key2,new_node.ptr)
        self.bin_capacity.root=self.bin_capacity.insert(new_node,self.bin_capacity.root)
        li=[]
        self.bin_capacity.in_order_traversal(self.bin_capacity.root,li)
        # print('inorder traversal after insert',li)
        new_node.ptr.avl.insert_node_2(obj.object_id,obj.size)
        new_node.ptr.capacity-=obj.size
        node_s=self.bin_id.search_id(self.bin_id.root,bin_id)
        node_s.key2-=obj.size
        object_id_node=self.object_id.search_id(self.object_id.root,obj.object_id)
        object_id_node.ptr=new_node.ptr
    def Largest_Least(self,obj:object,node:Node):
        node=self.bin_capacity.root
        curr=node
        # print(curr.right.key1)
        while curr.right!=None:
            curr=curr.right
        if curr.key1<obj.size:
            raise NoBinFoundException
        val=curr.key1
        node=self.search(self.bin_capacity.root,val)
        ans=node
        while node is not None:
            if node.key1==val:
                ans=node
                node=node.left
            elif node.key1<val:
                node=node.right
        node=ans
        new_size=node.key1-obj.size
        bin_id=node.key2
        new_node=Node(new_size,bin_id)
        new_node.ptr=node.ptr
        self.bin_capacity._delete_node(node,self.bin_capacity.root)
        # print(new_node.key1,new_node.key2,new_node.ptr)
        self.bin_capacity.root=self.bin_capacity.insert(new_node,self.bin_capacity.root)
        li=[]
        self.bin_capacity.in_order_traversal(self.bin_capacity.root,li)
        # print('inorder traversal after insert',li)
        new_node.ptr.avl.insert_node_2(obj.object_id,obj.size)
        new_node.ptr.capacity-=obj.size
        node_s=self.bin_id.search_id(self.bin_id.root,bin_id)
        node_s.key2-=obj.size
        object_id_node=self.object_id.search_id(self.object_id.root,obj.object_id)
        object_id_node.ptr=new_node.ptr
    def Largest_Max(self,obj:Object,node:Node):
        curr=node
        while curr.right!=None:
            curr=curr.right
        if curr.key1<obj.size:
            raise NoBinFoundException
        node=curr
        new_size=node.key1-obj.size
        bin_id=node.key2
        new_node=Node(new_size,bin_id)
        new_node.ptr=node.ptr
        self.bin_capacity._delete_node(node,self.bin_capacity.root)
        # print(new_node.key1,new_node.key2,new_node.ptr)
        self.bin_capacity.root=self.bin_capacity.insert(new_node,self.bin_capacity.root)
        li=[]
        self.bin_capacity.in_order_traversal(self.bin_capacity.root,li)
        # print('inorder traversal after insert',li)
        new_node.ptr.avl.insert_node_2(obj.object_id,obj.size)
        new_node.ptr.capacity-=obj.size
        node_s=self.bin_id.search_id(self.bin_id.root,bin_id)
        node_s.key2-=obj.size
        object_id_node=self.object_id.search_id(self.object_id.root,obj.object_id)
        object_id_node.ptr=new_node.ptr
    def compact_max(self,obj:object,node:Node):
        node1=self.bin_capacity.root
        curr=node1
        while curr.right!=None:
            curr=curr.right
        if curr.key1<obj.size:
            raise NoBinFoundException
        val=self.least_node(self.bin_capacity.root,obj.size).key1
        node=self.search(self.bin_capacity.root,val)
        ans=node
        while node is not None:
            if node.key1==val:
                ans=node
                node=node.right
            elif node.key1>val:
                node=node.left
        node=ans
        new_size=node.key1-obj.size
        bin_id=node.key2
        new_node=Node(new_size,bin_id)
        new_node.ptr=node.ptr
        self.bin_capacity._delete_node(node,self.bin_capacity.root)
        # print(new_node.key1,new_node.key2,new_node.ptr)
        self.bin_capacity.root=self.bin_capacity.insert(new_node,self.bin_capacity.root)
        li=[]
        self.bin_capacity.in_order_traversal(self.bin_capacity.root,li)
        # print('inorder traversal after insert',li)
        new_node.ptr.avl.insert_node_2(obj.object_id,obj.size)
        new_node.ptr.capacity-=obj.size
        node_s=self.bin_id.search_id(self.bin_id.root,bin_id)
        node_s.key2-=obj.size
        object_id_node=self.object_id.search_id(self.object_id.root,obj.object_id)
        object_id_node.ptr=new_node.ptr
    def add_bin(self, bin_id1, capacity1):
        cur_bin=Bin(bin_id1,capacity1)
        self.bin_id.insert_node_3(bin_id1,capacity1,cur_bin)
        self.bin_capacity.insert_node_3(capacity1,bin_id1,cur_bin)
        pass
    def add_object(self, object_id, size, color):
        cur_obj=Object(object_id, size, color)
        self.object_id.insert_node_2(object_id,size)
        if color==Color.RED: 
            self.Largest_Least(cur_obj,self.bin_capacity.root)
        elif (color==Color.GREEN):
            self.Largest_Max(cur_obj,self.bin_capacity.root)
        elif color==Color.BLUE:
            self.compact_min(cur_obj,self.bin_capacity.root)
        elif color==Color.YELLOW:
            self.compact_max(cur_obj,self.bin_capacity.root)
    # def delete_object(self,object_id):
    def delete_object(self, object_id):
        # # Implement logic to remove an object from its bin
        # my_obj = self.object_id.search_id(self.object_id.root,object_id) #node obtained which has the id of the particular object
        # obj_size= my_obj.key2
        # bin=my_obj.ptr #came to bin
        # li=[]
        # bin.avl.in_order_traversal(bin.avl.root,li)
        # print(li)
        # Bin_id= bin.bin_id
        # print('deleted object was',Bin_id,obj_size)
        # node=Node(object_id,obj_size)
        # # print(node.key1)
        # # bin.avl.search_id()
        # bin.avl._delete_node(node,bin.avl.root) #to check if this 0 works as the cap
        # li=[]
        # bin.avl.in_order_traversal(bin.avl.root,li)
        # print(li)
        # my_obj.ptr=None
        # node=Node(object_id,obj_size)
        # # print(type(node))
        # # print(node.key1,node.key2)
        # self.object_id._delete_node(node,self.object_id.root) #deleting the object from o_id avl tree

        # cur_bin_id=self.bin_id.search_id(self.bin_id.root,Bin_id) #node in b_id obtained of the bin cap in which deletion was made  
        # b_c=cur_bin_id.key2
        # cur_bin_id.key2+=obj_size
        # print('deleted object was',b_c,cur_bin_id.key2)
        # cur_bin_cap=self.bin_capacity.search_id(self.bin_capacity.root,b_c)
        # b_cap=cur_bin_cap.key1
        # b_iid=cur_bin_cap.key2
        # # self.b_cap.delete(cur_bin_cap.id,cur_bin_cap.key)
        # # self.b_cap.insert_node_2(b_cap,b_iid)
        # node=Node(b_cap+obj_size,b_iid)
        # node.ptr=cur_bin_cap.ptr
        # self.bin_capacity._delete_node(cur_bin_cap,self.bin_capacity.root)
        # # print(new_node.key1,new_node.key2,new_node.ptr)
        # self.bin_capacity.root=self.bin_capacity.insert(node,self.bin_capacity.root)
        
        # cur_bin_cap.key+=obj_size

        ##REBALANCE THE NODE
        # li=[]
        # self.bin_capacity_tree.inorder_traversal(self.bin_capacity_tree.root,li)
        # print(li)
        # search object in object_id tree
        node1=self.object_id.search_id(self.object_id.root,object_id,)
        # obtaining bin id
        # print('object to be deleted',object_id)
        bin_id=node1.ptr.bin_id
        # print(bin_id,object_id)
        # obtaining the object size
        obj_size=node1.key2
        # print(obj_size)
        # searching the bin id in bin id tree
        node2=self.bin_id.search_id(self.bin_id.root,bin_id)
        # obtaining bin capacity from bin id
        bin_capacity=node2.key2
        # print(bin_capacity,'bin capacity for that node in which it is stored')
        # searching bin capacity and bin id in the capacity tree
        
        node3=self.bin_capacity.search_id(self.bin_capacity.root,bin_capacity,)
        # deleting the node from capacity tree
        # print(node3.key1,'capacity',node3.key2,'bin_id')
        node4=Node(node3.key1+obj_size,node3.key2)
        self.bin_capacity._delete_node(node3,self.bin_capacity.root)
        # incrementing the capacity of node
        # li=[]
        # self.bin_capacity_tree.inorder_traversal(self.bin_capacity_tree.root,li)
        # print(li,'inorder traversal after delete')
        # print(node4.key1,node4.key2)
        # deleting node1 from object id tree
        self.object_id._delete_node(node1,self.object_id.root)
        node6=Node(object_id,obj_size)
        node2.ptr.avl._delete_node(node6,node2.ptr.avl.root)
        node2.key2+=obj_size
        # print(node2.key1,'bin_id',node2.key2,'bin_capacity')
        # reinserting the node in tree
        self.bin_capacity.insert(node4,self.bin_capacity.root)
        # Implement logic to remove an object from its bin
        pass

        pass

    def bin_info(self, bin_id):
        cur_bin_id = self.bin_id.search_id(self.bin_id.root,bin_id)
        cur_bin=cur_bin_id.ptr
        ans=[]
        cur_bin.avl.in_order_traversal(cur_bin.avl.root,ans)
        tup = (cur_bin.capacity,ans)

        return tup
    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        cur_o_id=self.object_id.search_id(self.object_id.root,object_id)
        cur_b=cur_o_id.ptr
        return cur_b.bin_id
        pass