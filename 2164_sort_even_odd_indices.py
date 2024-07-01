# heapq for odd and even indices
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ho = []
        he = []
        for i, n in enumerate(nums):
            if i % 2 == 0:
                heapq.heappush(he, n)
            else:
                heapq.heappush(ho, -n)
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = heapq.heappop(he)
            else:
                nums[i] = -heapq.heappop(ho)
        
        return nums