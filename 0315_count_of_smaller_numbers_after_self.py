# sorted list
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        h = sortedcontainers.SortedList([])
        n = len(nums)
        ans = [0] * n
        for i in range(len(nums)):
            a = nums[~i]
            j = bisect.bisect_left(h, a)
            ans[~i] = j
            h.add(a)
        return ans