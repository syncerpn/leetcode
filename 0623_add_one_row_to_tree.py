# easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        l = 2
        s = [root]
        while l <= depth:
            s_next = []
            for node in s:
                if l == depth:
                    node.left = TreeNode(val, left=node.left)
                elif node.left:
                    s_next.append(node.left)
                if l == depth:
                    node.right = TreeNode(val, right=node.right)
                elif node.right:
                    s_next.append(node.right)
            s = s_next
            l += 1
        return root