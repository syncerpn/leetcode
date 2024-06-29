# bfs + tree traversal approach O(nlogn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        s = [root]
        while s:
            s_next = []
            for i in s:
                if i.val != k - i.val:
                    j = root
                    while j:
                        if k - i.val == j.val:
                            return True
                        if k - i.val > j.val:
                            j = j.right
                        else:
                            j = j.left
                if i.left:
                    s_next.append(i.left)
                if i.right:
                    s_next.append(i.right)
            s = s_next
        return False