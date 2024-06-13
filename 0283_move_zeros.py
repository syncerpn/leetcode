#1. two pointers, tracking the zeros and iterating the array
def solve(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1