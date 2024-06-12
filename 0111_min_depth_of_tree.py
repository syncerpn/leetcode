#1. would you choose recursive?
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    if not root:
        return 0
        
    if not root.left and not root.right:
        return 1
    
    if root.left and root.right:
        return 1 + min(solve(root.left), solve(root.right))

    if root.left:
        return 1 + solve(root.left)
    
    return 1 + solve(root.right)

#1. or BFS?
def solve2(root: TreeNode) -> int:
    if not root:
        return 0
    
    queue = []
    i = 0
    l = 0
    d = 1
    if root.left:
        queue.append(root.left)
        l += 1
    if root.right:
        queue.append(root.right)
        l += 1
    m = l
    while queue:
        root = queue[i]
        if not root.left and not root.right:
            return d+1
        if root.left:
            queue.append(root.left)
            l += 1
        if root.right:
            queue.append(root.right)
            l += 1
            
        i += 1
        if i == m:
            m = l
            d += 1

    return d