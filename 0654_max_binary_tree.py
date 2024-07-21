# recursion makes it simple
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m = 0
        j = 0
        for i, n in enumerate(nums):
            if n > m:
                m = n
                j = i
        return TreeNode(m, left=self.constructMaximumBinaryTree(nums[:j]), right=self.constructMaximumBinaryTree(nums[j+1:]))