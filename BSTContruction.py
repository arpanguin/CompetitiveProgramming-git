# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        return self

    def contains(self, value):
        root_node = self
        while root_node:
            if value == root_node.value:
                return True
            if value > root_node.value:
                root_node = root_node.right
            elif value < root_node.value:
                root_node = root_node.left
        return False

    def remove(self, value):
        if not self.contains(value):
            return self
        root_node = self
        while root_node:
            if value > root_node.value:
                if root_node.right and root_node.right.value == value:
                    root_node.right = None
                else:
                    root_node = root_node.right
            elif value < root_node.value:
                if root_node.left and root_node.left.value == value:
                    root_node.left = None
                else:
                    root_node = root_node.left
            else:
                if not root_node.right and not root_node.left:
                    self = None
                    root_node = None
                else:
                    if root_node.right:
                        smallest_value = self.find_smallest(root_node.right)
                    elif root_node.left:
                        smallest_value = self.find_smallest(root_node.left)
                    self.remove(smallest_value)
                    root_node.value = smallest_value
        return self

    def find_smallest(self, root):
        while root:
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                return root.value


bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.remove(10)
print(bst.contains(15))