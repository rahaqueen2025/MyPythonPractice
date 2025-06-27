#class TreeNode:
#    def __init__(self,value):
#        self.value = value
#         self.children = []

#    def add_child(self,child_node):
#        self.children.append(child_node)

#    def display(self,level=0):
#        print(" " * level * 4 + str(self.value)) 
#        for child in self.children:
#            child.display(level + 1)

#root = TreeNode("Root")

#child1 =TreeNode("child 1")
#child2 =TreeNode("child 2")

#child1.add_child(TreeNode("Grandchild 1"))
#child1.add_child(TreeNode("Grandchild 2"))
#child2.add_child(TreeNode("Grandchild 3"))

#root.add_child(child1)
#root.add_child(child2)

#root.display()


class BinarySearchTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self ,new_value):
        if new_value < self.value:
            if not self.left:
                self.left =BinarySearchTree(new_value)
            else:
                self.left.insert(new_value)
        elif new_value > self.value:
            if not self.right:
                self.right = BinarySearchTree(new_value)
            else:
                self.right.insert(new_value)                    
    def display(self , level =0):
        if self.right:
            self.right.display(level + 1)
        print(" " * level * 4 + str(self.value))
        if self.left:
            self.left.display(level + 1)

root = BinarySearchTree(10) 
root.insert(8)
root.insert(12)
root.insert(11)
root.insert(9)
root.insert(14)
root.display()               