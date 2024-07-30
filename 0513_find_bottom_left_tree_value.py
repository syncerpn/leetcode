# it asks the bottom leftmost value, not the bottom value on the left of another node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        s = [root]
        ans = root.val
        while s:
            s_next = []
            for n in s:
                ans = n.val
                if n.right:
                    s_next.append(n.right)
                if n.left:
                    s_next.append(n.left)
            
            s = s_next
        return ans