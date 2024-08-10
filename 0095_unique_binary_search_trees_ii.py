# got it right in the first submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = list(range(1, n+1))
        def make_tree(l, r):
            if l == r:
                return [None]
            ans = []
            for m in range(l, r):
                for left in make_tree(l, m):
                    for right in make_tree(m+1, r):
                        ans.append(TreeNode(nums[m], left=left, right=right))
            return ans

        
        return make_tree(0, n)
