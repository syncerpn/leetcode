# bfs
# should be easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            t = []
            s_next = []
            for n in s:
                t.append(n.val)
                if n.left:
                    s_next.append(n.left)
                if n.right:
                    s_next.append(n.right)
            ans.append(t)
            s = s_next
        return ans