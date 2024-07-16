# sort, prefix sum, and binary search
# very good problem
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        return [bisect_right(nums, qi) for qi in queries]