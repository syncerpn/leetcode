# prefix must start at 0
# unclear desc costed me lots of time
# other than that, it is easy
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        d = set(nums)
        s = nums[0]
        p = nums[0]
        for n in nums[1:]:
            if n != p + 1:
                break
            s += n
            p = n
        
        while s in d:
            s += 1
        return s