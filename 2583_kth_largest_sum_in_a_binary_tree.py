# traverse and track level sums
# then sort, or use a heapq, or faster with quick select O(n)
# but i see them all as equivalence
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        s, r = [], [root]
        while r:
            r_next = []
            t = 0
            for node in r:
                t += node.val
                if node.left:
                    r_next.append(node.left)
                if node.right:
                    r_next.append(node.right)
            s.append(t)
            
            r = r_next
        if k > len(s):
            return -1
        s.sort(reverse=True)
        return s[k-1]