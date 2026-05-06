# nice problem
# went from a common prefix sum
# to tracking index (just like mod problem)
# and to accurately counting with hash map
# anyway still trivial to fix it gradually
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = list(accumulate(nums, initial=0))
        l = 0
        ans = 0
        d = {}
        for i, a in enumerate(P):
            if a not in d:
                d[a] = 0
            d[a] += 1
            if a - k in d:
                ans += d[a-k]
                if k == 0:
                    ans -= 1
        return ans