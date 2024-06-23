# traversal and check, non-recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def next_left(root):
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                
                root = stack.pop()
                root = root.right
                yield root

            yield None
        
        def next_right(root):
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.right
                
                root = stack.pop()
                root = root.left
                yield root

            yield None
        
        for node_l, node_r in zip(next_left(root), next_right(root)):
            if node_l and node_r:
                if node_l.val == node_r.val:
                    continue
                return False
            elif not node_l and not node_r:
                continue
            return False
        return True

# or recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l, r):
            if not l and not r:
                return True
                
            if not l or not r:
                return False
            
            return l.val == r.val and check(l.left, r.right) and check(l.right, r.left)
        
        return check(root.left, root.right)