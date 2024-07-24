# the logic is pretty much complicated if we try to follow the description
# to simplify it, we should only care about balancing subtree
# and a node in the tree may have negative balance (this is the key point)
#
# with example 1:
#   3
#  / \
# 0   0
# the left node needs 1 coin to balance and the right needs 1 coin
# so we count it as two moves to distribute
#
# with example 2
#   0
#  / \
# 3   0
# so the left node need -2 coin to balance (yes, it is negative number)
# and the right one need 1
# so we count it as abs(-2) + 1 = 3 moves
# 
# now as we understand the simplified logic, just traverse the network node to root
# counting how many coins (can be positive, and more importantly can be negative)
# needed to balance each subtree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def traverse(root, moves):
            if not root:
                return 0
            l = traverse(root.left, moves)
            r = traverse(root.right, moves)
            moves[0] += abs(l) + abs(r)
            return root.val + l + r - 1
            # as the logic suggest, we can also return this, which i think explains itself
            # return 1 - (root.val - l -r)
            # that we use root.val to distribute the needed coins of left and right
            # then, the remaining is root.val - l - r
            # now the root needs 1 - root.val to have 1 coins in the end
        
        moves = [0]
        traverse(root, moves)
        return moves[0]