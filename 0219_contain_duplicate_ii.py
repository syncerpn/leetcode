#1. using dict should be fine, O(N) space
def solve(nums: list, k: int) -> bool:
    d = {}
    for i, n in enumerate(nums):
        if n in d:
            if i - d[n] <= k:
                return True
        d[n] = i
    return False