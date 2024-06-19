# so, you can choose recursive or this one, merkle hashing
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        from hashlib import sha256
        def _hash(x):
            S = sha256()
            S.update(bytes(x, encoding='utf-8'))
            return S.hexdigest()
        
        def merkle(node):
            if not node:
                return "#"
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = _hash(m_left + str(node.val) + m_right)
            return node.merkle
        
        merkle(root)
        merkle(subRoot)
        def dfs(node):
            if not node:
                return False
            return node.merkle == subRoot.merkle or dfs(node.left) or dfs(node.right)
        
        return dfs(root)