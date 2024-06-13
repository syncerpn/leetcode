class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> str:        
    if not root.left and not root.right:
        return [f"{root.val}"]

    path = []
    if root.left:
        path += [f"{root.val}->" + i for i in solve(root.left)]
    
    if root.right:
        path += [f"{root.val}->" + i for i in solve(root.right)]
    
    return path