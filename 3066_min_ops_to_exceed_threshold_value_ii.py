# heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans = 0
        a = heapq.heappop(nums)
        while a < k:
            ans += 1
            b = heapq.heappop(nums) + 2 * a
            a = heapq.heappushpop(nums, b)
        return ans