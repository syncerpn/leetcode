# easy
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        s = [root]
        while s:
            s_next = []
            p = None
            for node in s:
                if p:
                    p.next = node
                p = node
                if node.left:
                    s_next.append(node.left)
                    s_next.append(node.right)
            s = s_next
        return root
