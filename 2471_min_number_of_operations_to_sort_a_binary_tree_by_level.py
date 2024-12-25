# simple use sorted indices to count the swapping turns
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        s = [root]
        while s:
            v = []
            s_next = []
            for i, n in enumerate(s):
                v.append(i)
                if n.left:
                    s_next.append(n.left)
                if n.right:
                    s_next.append(n.right)
            v.sort(key=lambda i: s[i].val)
            r = set(list(range(len(v))))
            while r:
                i = r.pop()
                j = i
                while v[j] != i:
                    j = v[j]
                    r.discard(j)
                    ans += 1
            s = s_next
        return ans