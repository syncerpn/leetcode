# standard way with binary search
# this is actually O(n2) just because
# passing a slice of array actually generates a new slices
# which takes O(n) time and space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        rv = preorder[0]
        k = bisect_right(preorder, rv)
        return TreeNode(rv, left=self.bstFromPreorder(preorder[1:k]), right=self.bstFromPreorder(preorder[k:]))

# this is true O(nlogn)
# which do everything with a single reference of "preorder"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(i, j):
            if i == j: return None
            mid = bisect.bisect(preorder, preorder[i], i + 1, j)
            return TreeNode(preorder[i], left=helper(i + 1, mid), right=helper(mid, j))
        return helper(0, len(preorder))

# it went crazier with O(n) solution
# but requires modifying the provided function with default param and global param
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    CONSTRAINTS_MAX = 1001
    i = 0
    def bstFromPreorder(self, preorder: List[int], bound=CONSTRAINTS_MAX) -> Optional[TreeNode]:
        if self.i == len(preorder) or preorder[self.i] > bound:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(preorder, root.val)
        root.right = self.bstFromPreorder(preorder, bound)
        return root