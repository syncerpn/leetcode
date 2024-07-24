# rebuild tree may not needed
# but still included
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        s = [root]
        while s:
            s_next = []
            for n in s:
                if n.left:
                    n.left.val = n.val * 2 + 1
                    s_next.append(n.left)
                if n.right:
                    n.right.val = n.val * 2 + 2
                    s_next.append(n.right)
            s = s_next
        self.root = root

    def find(self, target: int) -> bool:
        d = []
        while target:
            d.append(target % 2)
            target = (target + target % 2 - 2) // 2
        
        node = self.root
        while d:
            m = d.pop()
            if m == 1 and node.left:
                node = node.left
            elif m == 0 and node.right:
                node = node.right
            else:
                return False
        return True

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)