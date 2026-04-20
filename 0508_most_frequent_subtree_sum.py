# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        d = defaultdict(int)
        def subtree_sum(node):
            l, r = 0, 0
            if not node.left and not node.right:
                return node.val
            if node.left:
                l = subtree_sum(node.left)
                d[l] +=1
            if node.right:
                r = subtree_sum(node.right)
                d[r] += 1
            s = node.val + l + r
            return s
        
        s = subtree_sum(root)
        d[s] += 1
        m = max(d.values())
        return [k for k in d if d[k] == m]