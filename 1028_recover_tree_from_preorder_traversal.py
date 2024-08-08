# got it right after a few trials
# lol
# not that hard anyway
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        DIGITS = "0123456789"
        s = []
        d = 0
        d_curr = 0
        v = ""
        node = None
        root = None
        for c in traversal + "#":
            if c in DIGITS:
                v += c
            else:
                if root is None:
                    root = TreeNode(int(v))
                    node = root
                    s.append(root)
                    v = ""
                    d = 1
                else:
                    if v != "":
                        while d <= d_curr:
                            node = s.pop()
                            d_curr -= 1
                        if node.left is None:
                            node.left = TreeNode(int(v))
                            s.append(node)
                            node = node.left
                        else:
                            node.right = TreeNode(int(v))
                            s.append(node)
                            node = node.right
                        d_curr = d
                        d = 1
                        v = ""
                    else:
                        d += 1
        
        return root