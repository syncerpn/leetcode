# write this down to learn the logic first
# observation is that we will just choose an even-length subarray to rotate
# because there is always an equivalence to do so with choosing an odd-length subarray
# and more importantly, use prefix sum to determine the subarray sum
class Solution:
    def maxValue(self, nums: List[int]) -> int:
        p = [0]
        E, O = [], [0]
        for i, a in enumerate(nums):
            if i % 2:
                p.append(p[-1] - a)
                O.append(p[-1])
            else:
                p.append(p[-1] + a)
                E.append(p[-1])
        
        ans = p[-1]
        d = 0
        for Q in [E, O]:
            ma = -inf
            for a in Q:
                if a < ma:
                    d = min(d, a - ma)
                else:
                    ma = a
        return ans - 2 * d

# optimized runtime and space complexity
# but the same logic
# ma_o set to 0 initially
class Solution:
    def maxValue(self, nums: List[int]) -> int:
        ans = 0
        ma_e, ma_o = -inf, 0
        d = 0
        for i, a in enumerate(nums):
            if i % 2:
                ans -= a
                ma_o = max(ma_o, ans)
                d = min(d, ans - ma_o)
            else:
                ans += a
                ma_e = max(ma_e, ans)
                d = min(d, ans - ma_e)
        
        return ans - 2 * d