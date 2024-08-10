# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def helper(root, s, p):
            s -= root.val
            p.append(root.val)
            if not root.left and not root.right and s == 0:
                ans.append(p[:])
            
            if root.left:
                helper(root.left, s, p)
            if root.right:
                helper(root.right, s, p)
            p.pop()

        helper(root, targetSum, [])
        return ans