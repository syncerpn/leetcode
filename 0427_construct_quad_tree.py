# check whether mat contains mixed value
# if not, create a leaf from mat
# else, recursively construct quad tree
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        grid_val = sum(grid, [])
        if all(grid_val) or not any(grid_val):
            return Node(grid[0][0], 1, None, None, None, None)
        
        n = len(grid)
        tl = [g[:n//2] for g in grid[:n//2]]
        tr = [g[n//2:] for g in grid[:n//2]]
        bl = [g[:n//2] for g in grid[n//2:]]
        br = [g[n//2:] for g in grid[n//2:]]
        return Node(1, 0, self.construct(tl), self.construct(tr), self.construct(bl), self.construct(br))