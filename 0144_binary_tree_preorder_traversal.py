#1. recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> list:
    if not root:
        return []
    
    return [root.val] + solve(root.left) + solve(root.right)

#1. or iterative with BFS and stack push pop
def solve2(root: TreeNode) -> list:
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        root = stack.pop()
        result.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

    return result