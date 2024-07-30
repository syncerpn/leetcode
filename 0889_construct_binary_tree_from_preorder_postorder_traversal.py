# not that difficult
# we just need to break traversal orders into those belong to left and right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        l = 0
        while l < len(postorder)-1:
            if postorder[l] == preorder[1]:
                root.left = self.constructFromPrePost(preorder[1:1+l+1], postorder[:l+1])
                break
            l += 1
        if l < len(postorder)-2:
            root.right = self.constructFromPrePost(preorder[1+l+1:], postorder[l+1:-1])
        return root