# easy with bfs
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        s = [root]
        while s:
            s_next = []
            l = []
            for n in s:
                l.append(n.val)
                if n.children:
                    s_next += n.children
            ans.append(l)
            s = s_next
        return ans