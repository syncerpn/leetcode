# priority queue is the solution
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for n in nums:
            heapq.heappush(self.h, n)
            while len(self.h) > k:
                heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)