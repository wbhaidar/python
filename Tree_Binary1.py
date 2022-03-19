

from types import NoneType


class Tree:
    def __init__(self, val = None):
        if val == None:
            self.val = None
        else:
            self.val = val
        self.left = None
        self.right = None

    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree()
                    self.left.val = val
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Tree()
                    self.right.val = val
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def print_in_order_traversal(self):
        if self.left:
            self.left.print_in_order_traversal()
        
        print(self.val)
        
        if self.right :
                self.right.print_in_order_traversal()
             





tree =Tree(20)
print(tree)
tree.insert(18)
tree.insert(22)
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)

tree.print_in_order_traversal()
