# bruteforce
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            m = inf
            a = -1
            for r in range(l, n):
                m = min(m, nums[r])
                a = a & nums[r]
                if a == m:
                    ans += 1
        return ans