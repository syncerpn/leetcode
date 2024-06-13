class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    l = root.left
    r = root.right
    root.left = invertTree(r)
    root.right = invertTree(l)
    return root