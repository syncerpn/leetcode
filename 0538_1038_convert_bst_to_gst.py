# dfs + stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = 0
        stack = []
        node = root
        # starting from root
        while stack or node:
            # keep going right if possible
            while node:
                stack.append(node)
                node = node.right

            # if no more right, travel up one level, add its val to acc, and update its val with acc
            node = stack.pop()
            node.val += acc
            acc = node.val
            # then go left
            node = node.left
        
        return root
        