# quite similar to #0502, which heapq can solve it
# there is a simpler way as well that tracks staircase [difficulty: max profit]
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        h = []
        for p, d in zip(profit, difficulty):
            heapq.heappush(h, (-p, d))

        w = sorted(worker, reverse=True)

        total_profit = 0
        p, d = heapq.heappop(h)

        for i, wi in enumerate(w):
            while h and d > wi:
                p, d = heapq.heappop(h)
            
            if d <= wi:
                total_profit -= p
        
        return total_profit