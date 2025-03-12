# recursive solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        return root if l and r else l or r

# or build path but is much slower
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path(root, p):
            if root:
                if root == p:
                    return [root]
                s = path(root.left, p)
                if s:
                    return s + [root]
                s = path(root.right, p)
                if s:
                    return s + [root]
            return []
        
        sp = set(path(root, p))
        sq = path(root, q)
        for qi in sq:
            if qi in sp:
                return qi
        
        return None

