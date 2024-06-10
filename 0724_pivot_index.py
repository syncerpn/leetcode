#1. prefix sum obviously
#2. adjust the sum as iterating the list to reflect left and right sum
def solve(nums: list) -> int:
    total = 0
    for n in nums:
        total += n
    
    left = 0
    for i, n in enumerate(nums):
        total -= n
        if total == left:
            return i
        left += n
    
    return -1