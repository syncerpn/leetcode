# tracking which parent a node is as well to get the replacement
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [(0, root)]
        while s:
            s_next = []
            t = 0
            i = 0
            d = {}
            for i, jn in enumerate(s):
                j, n = jn
                t += n.val
                if j not in d:
                    d[j] = 0
                d[j] += n.val
                if n.left:
                    s_next.append((i, n.left))
                if n.right:
                    s_next.append((i, n.right))
            
            for j, n in s:
                n.val = t - d[j]
            
            s = s_next

        return root