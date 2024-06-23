# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        m = n // 2
        root = TreeNode(nums[m], self.sortedArrayToBST(nums[:m]), self.sortedArrayToBST(nums[m+1:]))
        return root