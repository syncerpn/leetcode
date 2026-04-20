# easy
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        p, P = -inf, []
        s, S =  inf, []
        n = len(nums)
        for i in range(n):
            p = max(p, nums[i])
            P.append(p)
            s = min(s, nums[~i])
            S.append(s)
        
        for i in range(n):
            if P[i] - S[~i] <= k:
                return i
        return -1