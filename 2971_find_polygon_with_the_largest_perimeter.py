# sort O(1) space
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = sum(nums)
        for i in range(n-1, 0, -1):
            if s > 2 * nums[i]:
                return s
            s -= nums[i]
        return -1

# it can be O(n + 30logn) time ~ O(n)
# by using max heap
# i also learned that building a heap from a predefined sequence is O(n) instead of O(nlogn)
# the difference is that "predefined"
# instead of building an empty heap then adding elements one by one
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s = sum(nums)
        heapq._heapify_max(nums)
        while nums and s <= nums[0] * 2:
            s -= heapq._heappop_max(nums)
        return s if len(nums) > 2 else -1