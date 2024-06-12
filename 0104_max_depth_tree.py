#1. i realized, tree is about recursive algorithm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    if not root:
        return 0
    
    return 1 + max(solve(root.left), solve(root.right))