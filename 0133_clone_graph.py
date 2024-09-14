# recursive dfs is powerful
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        d = {}
        def create_node(node):
            d[node.val] = Node(node.val)
            for n in node.neighbors:
                if n.val not in d:
                    d[node.val].neighbors.append(create_node(n))
                else:
                    d[node.val].neighbors.append(d[n.val])
            
            return d[node.val]

        return create_node(node)