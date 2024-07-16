# single traversal
# we use dfs to build path from root to start and root to dest
# the we need to find the longest common ancestor between the two paths
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
                # dfs, keep going left
                if node.val == startValue:
                    ps = p[:]
                if node.val == destValue:
                    pd = p[:]
                if ps and pd:
                    # if both paths are found, we can terminate traversal here
                    break
                s.append(node)
                p.append("L")
                node = node.left
            else:
                # until we cannot
                # then traversal up and change direction from left to right
                node = s.pop()
                node = node.right
                # if the up-one-level node is already on the right
                # keep moving up more
                while p and p[-1] == "R":
                    p.pop()
                # now as we reach to a left path, change its direction
                p[-1] = "R"
                # and repeat going left
                continue
            break
        
        # now is the time to find longest common ancestors, lca
        k = 0
        while k < len(ps) and k < len(pd):
            if ps[k] != pd[k]:
                break
            k += 1
        # the remaining uncommon, root to start path turns into going-up path
        # and root to dest path can be appended
        pd = ["U" * (len(ps) - k)] + pd[k:]
        return "".join(pd)