# (ALSO CHECK OUT MORRIS TRAVERSAL)
# thanks to the tree constraints, root is the minimum
# try to bfs the tree to find the next one that is bigger than root
# we only need to keep going with nodes whose val equals to root val
# because it is guaranteed that a root is always smaller than its children if any
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if not root.left:
            return -1
        m = -1
        s = [root]
        while s:
            node = s.pop()
            if node.left: # if left exists then right also exists
                # whether we need to go deeper from the left child
                if node.left.val == root.val:
                    s.append(node.left)
                # if a good value is found, update it to m, which we will return in the end
                elif m == -1:
                    m = node.left.val
                elif m > node.left.val:
                    m = node.left.val
                
                # and we do the same with the right child
                if node.right.val == root.val:
                    s.append(node.right)
                elif m == -1:
                    m = node.right.val
                elif m > node.right.val:
                    m = node.right.val
        return m
