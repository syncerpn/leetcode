# easy for brute-force
# solved with prefix max for efficiency
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n < 3:
            return nums
        
        L, l = [], -inf
        R, r = [], -inf
        for i in range(n):
            l = max(l, nums[i])
            L.append(l)
            r = max(r, nums[~i])
            R.append(r)
        ans = [nums[0]]
        for i in range(1, n-1):
            if nums[i] > L[i-1] or nums[i] > R[n-2-i]:
                ans.append(nums[i])
        ans.append(nums[-1])
        return ans