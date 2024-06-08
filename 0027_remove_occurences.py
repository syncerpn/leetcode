#1. two pointers, one iterates over nums and another keeps track of non-target values
def solve(nums: list, val: int) -> int:
    k = 0
    for n in nums:
        if n != val:
            nums[k] = n
            k += 1
    
    return k