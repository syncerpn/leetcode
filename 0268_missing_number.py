#1. use pure math
def solve(nums: list) -> int:
    x = 0
    for i, n in enumerate(nums):
        x ^= i ^ n
    return x ^ (i+1)

#1. or bit manip
def solve2(nums: list) -> int:
    return len(nums) * (len(nums)+1) // 2 - sum(nums)