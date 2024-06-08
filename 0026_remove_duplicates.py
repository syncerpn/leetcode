#1. two pointers tracking, one iterates over the nums and another keeps track of the numbers of unique value
def removeDuplicates(self, nums: List[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        n = nums[i]
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    
    return k