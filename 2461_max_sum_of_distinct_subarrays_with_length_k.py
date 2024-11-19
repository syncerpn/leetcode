# use one dict and one set
# or just use one dict but remove the keys with zero count
# a valid subarray should be any moment the length of the set (or dict if using one dict)
# equals k
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d, s = {}, 0
        ans = 0
        for i, n in enumerate(nums):
            if i >= k:
                p = nums[i-k]
                s -= p
                d[p] -= 1
                if d[p] == 0:
                    del d[p]

            s += n
            if n not in d:
                d[n] = 0
            d[n] += 1
            if len(d) == k:
                ans = max(ans, s)
        return ans