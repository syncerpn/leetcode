#1. implement leaf sequence get function
#2. may use recursive or stack
#3. the simply compare the leaf sequence

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root1: TreeNode, root2: TreeNode) -> bool:
    def get_leaf_sequence(root):
        ls = []
        stack = [None]
        node = root
        while node:
            if not node.left and not node.right:
                ls.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            node = stack.pop()
        return ls
    
    return get_leaf_sequence(root1) == get_leaf_sequence(root2)