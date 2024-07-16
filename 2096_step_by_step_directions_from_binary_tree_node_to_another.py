# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        p, ps, pd = [], [], []
        s = []
        node = root
        while s or node:
            while node:
                if node.val == startValue:
                    ps = p[:]
                if node.val == destValue:
                    pd = p[:]
                if ps and pd:
                    break
                s.append(node)
                p.append("L")
                node = node.left
            else:
                node = s.pop()
                node = node.right
                while len(p) > len(s):
                    p.pop()
                p.append("R")
                continue
            break
        
        k = 0
        while k < len(ps) and k < len(pd):
            if ps[k] != pd[k]:
                break
            k += 1
        pd = ["U" * (len(ps) - k)] + pd[k:]
        return "".join(pd)
