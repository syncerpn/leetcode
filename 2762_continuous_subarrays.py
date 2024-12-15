# monostack to keep track of min and max of sliding-window subarrays
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        smin = deque()
        smax = deque()
        ans = 0
        l = 0
        for (i, n) in enumerate(nums):
            while smin and nums[smin[-1]] > n:
                smin.pop()
            smin.append(i)
            while smax and nums[smax[-1]] < n:
                smax.pop()
            smax.append(i)
            while nums[smax[0]] - nums[smin[0]] > 2:
                if smax[0] < smin[0]:
                    l = smax.popleft() + 1
                else:
                    l = smin.popleft() + 1
            ans += i - l + 1
        return ans