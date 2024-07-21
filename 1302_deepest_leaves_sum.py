# bfs obviously
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        s = [root]
        while s:
            s_next = []
            for n in s:
                if n.left:
                    s_next.append(n.left)
                if n.right:
                    s_next.append(n.right)
            
            if not s_next:
                break
            s = s_next
        return sum([n.val for n in s])