# try to queue right leaf first then left leaf
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        s, ans = [root], []
        while s:
            found = False
            s_next = []
            for node in s:
                if node:
                    if not found:
                        ans.append(node.val)
                        found = True
                    s_next.append(node.right)
                    s_next.append(node.left)
            s = s_next
        return ans