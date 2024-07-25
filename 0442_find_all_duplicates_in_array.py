# use the same encoding as in #0448
# just beautiful
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            k = nums[abs(n)-1]
            if k < 0:
                res.append(abs(n))
            nums[abs(n)-1] = -k
        
        return res
        