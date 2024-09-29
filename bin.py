from avl import AVLTree
from node import Node
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.avl=AVLTree()
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        # self.bin_N.avlt.insert(object)


        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        pass
# bin=Bin(1234,10)
# print(bin.get_bin())