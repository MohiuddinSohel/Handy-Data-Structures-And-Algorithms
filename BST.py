class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def searchBST_recursive(self, root, val):
        if  not root:
            return root
        elif root.val == val :
            return root
        elif root.val > val:
            return self.searchBST_recursive(root.left, val)
        else:
            return self.searchBST_recursive(root.right, val)

    def searchBST_iterative(self, root, val):
        if  not root:
            return root
        while root:
            if root.val == val :
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    def insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        elif node.val > val:
            node.left = self.insert_recursive(node.left, val)
        else:
            node.right = self.insert_recursive(node.right, val)
        return node

    def insert_iterative(self, root, val):
        node = root
        if not node:
            return TreeNode(val)
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
        return root

    def getPreDecessor(root, target):
        if target.left:
            current = target.left
            while current.right:
                current = current.right
            return current
        else:
            current, predecessor = root, None
            while current:
                if current.val == target.val:
                    return predecessor
                elif current.val > target.val:
                    current = current.left
                else:
                    predecessor = current
                    current = current.right
            return predecessor

    def inOrderSuccessor(self, root, target):
        if target.right:
            current = target.right
            while current.left:
                current = current.left
            return current
        else:
            current, successor = root, None
            while current:
                if current.val > target.val:
                    successor = current
                    current = current.left
                elif current.val == target.val:
                    return successor
                else:
                    current = current.right
            return successor

    def deleteN(self, node, key):
        if not node:
            return None
        elif key < node.val:
            node.left = self.deleteN(node.left, key)
        elif key > node.val:
            node.right = self.deleteN(node.right, key)
        else:
            if not node.left and not node.right:
                return None
            elif node.right:
                successor = self.inOrderSuccessor(node, key)
                node.val = successor.val
                node.right = self.deleteN(node.right, successor.val)
            else:  # node must have left
                predecessor = self.getPreDecessor(node, key)
                node.val = predecessor.val
                node.left = self.deleteN(node.left, predecessor.val)
        return node
