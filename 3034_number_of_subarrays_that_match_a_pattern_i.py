# input is easy enough for this slow version
# if input is bigger, we need KMP algorithm
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        qs = [0 if a == b else (1 if a < b else -1) for a, b in pairwise(nums)]
        m, n = len(qs), len(pattern)
        ans = 0
        for i in range(m-n+1):
            for j in range(n):
                if qs[i+j] != pattern[j]:
                    break
            else:
                ans += 1
        return ans