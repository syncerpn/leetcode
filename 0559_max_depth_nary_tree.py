#1. recursive checking depth of children
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def solve(root) -> int:
    if not root:
        return 0
    if not root.children:
        return 1
    return 1 + max([solve(n) for n in root.children])
