# happy i solved it myself
# not really that hard though
# we traverse leaf to root, trying to return kind of cooldown during traversal
# a leaf (with no children) returns 0 to its parent
# saying that a camera is needed
# whenever a parent got 0 signal, we assign a camera to it
# now cooldown of 2 send to parent's parent, meaning that the parent's parent
# is covered by the camera we just assigned
# 0 signal is at highest priority
# then if there is 2, we dont need to care at the moment
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def traverse(root, n):
            if not root:
                return 1
            l = traverse(root.left, n)
            r = traverse(root.right, n)
            if l == 0 or r == 0:
                n[0] += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0
        
        n = [0]
        if traverse(root, n) == 0:
            n[0] += 1

        return n[0]
        