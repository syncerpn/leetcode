# my solution without recursion
# dfs, saving to be deleted node and its parent
# then try deleting bottom-up
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []
        s = []
        m = []
        node = root
        while s or node:
            while node:
                s.append(node)
                if node.left and node.left.val in to_delete:
                    m.append((node, node.left))
                node = node.left
            node = s.pop()
            if node.right and node.right.val in to_delete:
                m.append((node, node.right))
            node = node.right
        
        for n in m:
            print(n[0].val)

        while m:
            p, c = m.pop()
            if p.left == c:
                p.left = None
            else:
                p.right = None

            if c.left:
                forest.append(c.left)
            if c.right:
                forest.append(c.right)

        if root.val not in to_delete:
            forest.append(root)
        else:
            if root.left:
                forest.append(root.left)
            if root.right:
                forest.append(root.right)
        return forest

# bfs recursion solution is clean
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []

        # helper bfs traversal
        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete
            # make sure if the current "root" is actually a root and not in delete list
            # then it should be in the forest
            if is_root and not root_deleted:
                res.append(root)

            # if "root" is not in delete list
            # then its children are not new roots
            # otherwise they are
            # brilliant point
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        
        helper(root, True)
        return res