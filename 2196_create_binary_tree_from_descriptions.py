# quick lookup with hash table is pretty trivial
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        root = set()
        non_root = set()
        for p, c, l in descriptions:
            node_c = None
            if c in d:
                node_c = d[c]
            else:
                node_c = TreeNode(c)
                d[c] = node_c
                
            node_p = None
            if p in d:
                node_p = d[p]
            else:
                node_p = TreeNode(p)
                d[p] = node_p
            
            if l:
                node_p.left = node_c
            else:
                node_p.right = node_c

            non_root.add(c)
            root.add(p)
        
        r = list(root.difference(non_root))
        return d[r[0]]
