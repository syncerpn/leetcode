# recursion works well
# might add memoi to avoid redundant computation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        if n == 1:
            return [TreeNode()]
        if n == 3:
            return [TreeNode(0, left=TreeNode(), right=TreeNode())]
        
        result = []
        for i in range(1, n-1):
            j = n - 1 - i
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(j):
                    result.append(TreeNode(0, left=l, right=r))
        
        return result