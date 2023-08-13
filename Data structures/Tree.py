class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.leftNode = None
        self.rightNode = None


class SearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)
        
        if val < root.val:
            root.leftNode = self.insert(root.leftNode, val)
        elif val > root.val:
            root.rightNode = self.insert(root.rightNode, val)

        return root
    
bst = SearchTree()
bst.root = bst.insert(bst.root, 4)
bst.root = bst.insert(bst.root, 5)
bst.root = bst.insert(bst.root, 3)


print(bst.root.leftNode.val)
