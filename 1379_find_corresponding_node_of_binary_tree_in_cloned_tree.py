# just search with bfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s = [cloned]
        while s:
            s_next = []
            for node in s:
                if node.val == target.val:
                    return node
                if node.left:
                    s_next.append(node.left)
                if node.right:
                    s_next.append(node.right)
            
            s = s_next
        return None