# dfs + list/hash map
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]
        def helper(path_sum, node):
            if node:
                if node.val == targetSum:
                    ans[0] += 1
                if targetSum - node.val in path_sum:
                    ans[0] += path_sum[targetSum - node.val]
                path_sum_next = {p + node.val: path_sum[p] for p in path_sum}
                if node.val not in path_sum_next:
                    path_sum_next[node.val] = 0
                path_sum_next[node.val] += 1

                if node.left:
                    helper(path_sum_next, node.left)
                if node.right:
                    helper(path_sum_next, node.right)
                    
        helper({}, root)
        return ans[0]