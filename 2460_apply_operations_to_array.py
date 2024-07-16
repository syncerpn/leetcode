# likely single pass
# append on the way
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i]:
                r.append(nums[i])
        
        r.append(nums[-1])
        return r + [0] * (len(nums) - len(r))