#1. recursion is trivial? yes, it is
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

#1. "Recursive solution is trivial, could you do it iteratively?"
#2. since you asked:
def solve2(root: TreeNode) -> int:
    inorder_path = []
    stack = []
    while root or stack:
        #trying going left-most of the root
        while root:
            stack.append(root)
            root = root.left
        #until cannot proceed further, root is now None
        #go back one level, write down the val, go right, and repeat
        root = stack.pop()
        inorder_path.append(root.val)
        root = root.right

    return inorder_path