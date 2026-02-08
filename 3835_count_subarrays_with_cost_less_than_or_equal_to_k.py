# pretty classic sliding window
# how many subarrays with r-index ending?
# need to track next max, next min as elements are being removed gradually
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ma, mi = deque(), deque()
        ans = 0
        for r, a in enumerate(nums):
            while ma and ma[-1] < a:
                ma.pop()
            ma.append(a)

            while mi and mi[-1] > a:
                mi.pop()
            mi.append(a)

            while l <= r and (ma[0] - mi[0]) * (r - l + 1) > k:
                if ma[0] == nums[l]:
                    ma.popleft()
                if mi[0] == nums[l]:
                    mi.popleft()
                l += 1
            ans += r - l + 1
        return ans