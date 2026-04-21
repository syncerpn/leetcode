# easy
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        n = len(nums)
        ans = [0]
        ma = s
        l, r = 0, s
        for i in range(n):
            if nums[i] == 0:
                l += 1
            else:
                r -= 1
            t = l + r
            if t > ma:
                ma = t
                ans = [i+1]
            elif t == ma:
                ans.append(i+1)
        return ans