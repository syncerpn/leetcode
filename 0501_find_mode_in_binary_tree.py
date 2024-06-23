# simply traversal and count
# maybe inorder traversal could improve, but i am not really interested
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node):
            if not node:
                return []
            return [node.val] + traversal(node.left) + traversal(node.right)

        d = {}
        node_vals = traversal(root)
        v_max = 0
        for v in node_vals:
            if v not in d:
                d[v] = 0
            d[v] += 1
            if v_max < d[v]:
                v_max = d[v]
        
        res = []
        for k in d:
            if d[k] == v_max:
                res.append(k)

        return res