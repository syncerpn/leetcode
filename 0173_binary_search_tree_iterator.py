# implemented the follow-up question with average O(1) time for next() and O(h) memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.node = root
        self.s = []
        while self.node.left:
            self.s.append(self.node)
            self.node = self.node.left

    def next(self) -> int:
        v = self.node.val
        # prepare next node before  
        if self.node.right:
            self.node = self.node.right
            while self.node.left:
                self.s.append(self.node)
                self.node = self.node.left
        elif self.s:
            self.node = self.s.pop()
        else:
            self.node = None
        return v

    def hasNext(self) -> bool:
        return self.node is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()