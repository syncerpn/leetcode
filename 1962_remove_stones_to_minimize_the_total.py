# heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-a for a in piles]
        heapq.heapify(piles)
        while piles and k > 0:
            a = heapq.heappop(piles)
            a = -(abs(a) - abs(a) // 2)
            heapq.heappush(piles, a)
            k -= 1
        return -sum(piles)