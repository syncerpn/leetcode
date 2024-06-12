#1. recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> list:
    if not root:
        return []
    
    return solve(root.left) + solve(root.right) + [root.val]

#1. or iterative? this one is quite beautiful appending result to the left
def solve2(root: TreeNode) -> list:
    if not root:
        return []
    
    result = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            result = [root.val] + result
            root = root.right
        else:
            root = stack.pop()
            root = root.left

    return result