# merge sort with inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder_traversal(node):
            if not node:
                return []
            l, r = [], []
            if node.left:
                l = inorder_traversal(node.left)
            if node.right:
                r = inorder_traversal(node.right)
            return l + [node.val] + r
        
        vals1 = inorder_traversal(root1)
        vals2 = inorder_traversal(root2)
        i, j = 0, 0
        ans = []
        while i < len(vals1) and j < len(vals2):
            if vals1[i] < vals2[j]:
                ans.append(vals1[i])
                i += 1
            else:
                ans.append(vals2[j])
                j += 1
        if i < len(vals1):
            ans += vals1[i:]
        if j < len(vals2):
            ans += vals2[j:]
        return ans

# one-pass with iterator (see #0173 for more details)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def iterator(root):
            if not root:
                return []
            node = root
            s = []
            while node.left:
                s.append(node)
                node = node.left
            s.append(node)
            return s

        def next(s):
            if s:
                node = s.pop()
                v = node.val
                if node.right:
                    node = node.right
                    while node.left:
                        s.append(node)
                        node = node.left
                    s.append(node)
                return v
            else:
                return None
        s1 = iterator(root1)
        s2 = iterator(root2)
        v1 = next(s1)
        v2 = next(s2)
        ans = []
        while v1 is not None or v2 is not None:
            if v1 is None:
                ans.append(v2)
                v2 = next(s2)
            elif v2 is None:
                ans.append(v1)
                v1 = next(s1)
            elif v1 < v2:
                ans.append(v1)
                v1 = next(s1)
            else:
                ans.append(v2)
                v2 = next(s2)
        return ans