# trick to remove duplicates is good
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(ans)
            for j in range(len(ans)-l, len(ans)):
                ans.append(ans[j] + [nums[i]])
        
        return ans
        