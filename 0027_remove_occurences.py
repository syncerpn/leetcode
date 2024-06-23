# two pointers, one iterates over nums and another keeps track of non-target values
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        
        return k