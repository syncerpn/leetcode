# bfs
# calculate accumulate and average during traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        
        r = []
        s = [root]
        while s:
            s_next = []
            c = len(s)
            a = 0
            for n in s:
                a += n.val
                if n.left:
                    s_next.append(n.left)
                if n.right:
                    s_next.append(n.right)
            
            r.append(a/c)
            s = s_next
        
        return r