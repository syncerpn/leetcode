#1. using complete binary tree property to optimize counting
#2. where, if left depth and right depth are the same, tree has 2^depth - 1
#3. otherwise, recursive counting
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root) -> int:
    if not root:
        return 0
    
    ld = left_depth(root)
    rd = right_depth(root)
    if ld == rd:
        return (1 << ld) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

def left_depth(root):
    h = 0
    while root:
        root = root.left
        h += 1
    return h

def right_depth(root):
    h = 0
    while root:
        root = root.right
        h += 1
    return h