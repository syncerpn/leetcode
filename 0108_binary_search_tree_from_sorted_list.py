class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(nums: list) -> TreeNode:
    n = len(nums)
    if n == 0:
        return None
    m = n // 2
    root = TreeNode(nums[m], solve(nums[:m]), solve(nums[m+1:]))
    return root