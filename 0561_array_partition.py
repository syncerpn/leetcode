#1. pairing to eliminate as many small numbers as possible
#2. we can do so by sorting and pairing from smallest to the largest
def solve(nums: list) -> int:
    nums.sort()
    return sum(nums[0::2])