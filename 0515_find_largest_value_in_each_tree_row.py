# actually quite easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            s = [root]
            while s:
                m = -float("inf")
                s_next = []
                for n in s:
                    m = max(m, n.val)
                    if n.left:
                        s_next.append(n.left)
                    if n.right:
                        s_next.append(n.right)
                ans.append(m)
                s = s_next
        return ans