class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> bool:
    def get_height(root):
        if not root:
            return 0
        return 1 + max(get_height(root.left), get_height(root.right))
    
    if not root:
        return True
    
    if not solve(root.left):
        return False
    
    if not solve(root.right):
        return False

    return abs(get_height(root.left) - get_height(root.right)) <= 1