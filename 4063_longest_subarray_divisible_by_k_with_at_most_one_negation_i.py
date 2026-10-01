# easy O(n2)
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0

        p = 0
        d = {0:-1}
        for i in range(n):
            p += nums[i]
            m = p % k
            if m not in d:
                d[m] = i
            ans = max(ans, i - d[m])

        for i in range(n):
            p = 0
            d = {0:-1}
            for j in range(n):
                if i == j:
                    p -= nums[j]
                else:
                    p += nums[j]
                m = p % k
                if m not in d:
                    d[m] = j
                ans = max(ans, j - d[m])
        return ans