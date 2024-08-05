# go right until the end
# because once appended, the new val is at the end of the list
# so it should be on the right of any subtree
# except when itself is the new root of a subtree (only happend when it is a leaf)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            return TreeNode(val, left=root)

        n = root.right
        r = root
        while n:
            if n.val < val:
                nn = TreeNode(val, left=n)
                r.right = nn
                break
            r, n = n, n.right
        else:
            r.right = TreeNode(val)

        return root