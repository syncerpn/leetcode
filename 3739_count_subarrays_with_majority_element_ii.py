# O(n) solution is beautiful
# lee's solution is fancy yet difficult to understand at the same time
# it converts into balancing such that we track the difference between number of targets and number of non-targets
# by tracking this balance, we then want to find all prefix-(sum)balances that is smaller than the current one
# (so that we can take the current one minus each smaller and result in a subarray with majority of targets)
# it is a ordered map solution with a special implementation using array with negative indices
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = [1] + [0] * (n + n + 2)
        acc = [1] + [0] * (n + n + 2)
        ans = p = 0
        for a in nums:
            p += 1 if a == target else -1
            count[p] += 1
            acc[p] = acc[p-1] + count[p]
            ans += acc[p-1]
        return ans

# same idea as above but implemented as sorted list so the time is O(nlogn), worse than Lee'solution
# yet is easier to understand
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        p, ans, bst = 0, 0, sortedcontainers.SortedList([0])
        for a in nums:
            p += 1 if a == target else -1
            ans += bst.bisect_left(p)
            bst.add(p)
        return ans