# merge sort
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder_traversal(node):
            if not node:
                return []
            l, r = [], []
            if node.left:
                l = inorder_traversal(node.left)
            if node.right:
                r = inorder_traversal(node.right)
            return l + [node.val] + r
        
        vals1 = inorder_traversal(root1)
        vals2 = inorder_traversal(root2)
        i, j = 0, 0
        ans = []
        while i < len(vals1) and j < len(vals2):
            if vals1[i] < vals2[j]:
                ans.append(vals1[i])
                i += 1
            else:
                ans.append(vals2[j])
                j += 1
        if i < len(vals1):
            ans += vals1[i:]
        if j < len(vals2):
            ans += vals2[i:]
        return ans