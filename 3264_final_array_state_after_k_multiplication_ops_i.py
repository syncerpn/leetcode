# heapq solution
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(h)
        while k:
            n, i = heapq.heappop(h)
            n *= multiplier
            heapq.heappush(h, (n, i))
            k -= 1
        while h:
            n, i = heapq.heappop(h)
            nums[i] = n
        return nums
        