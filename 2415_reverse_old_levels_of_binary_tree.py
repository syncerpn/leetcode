# it is assumed perfect binary tree
# at even-level, save child nodes val into stack
# at odd-level, pop from stack to replace nodes val
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = [root]
        l = 0
        v = []
        while s:
            s_next = []
            for node in s:
                if not node:
                    return root
                if l % 2 == 0 and node.left:
                    v.append(node.left.val)
                    v.append(node.right.val)
                elif l % 2 == 1:
                    node.val = v.pop()
                s_next.append(node.left)
                s_next.append(node.right)
            l += 1
            s = s_next