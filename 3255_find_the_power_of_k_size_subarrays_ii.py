# same as #3254
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        c = 1
        n = len(nums)
        if k == 1:
            return nums
        ans = []
        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                c += 1
            else:
                c = 1
            if c >= k:
                ans.append(nums[i])
            elif i >= k-1:
                ans.append(-1)
        return ans