#1. recursive as usual
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    if root.left:
        if solve(root.left, targetSum - root.val):
            return True
    
    if root.right:
        if solve(root.right, targetSum - root.val):
            return True

    return False