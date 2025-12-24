# simple heap is the solution
# fairly easy at the first sight
# yet might take some time to finally converge to this solution
# initial thought's failed test case is 
# nums = [8,8,5,3,2,9,8,1,5,6]
# s = "1100100101"
# expected = 38
# (wrong) output = 39 lol
class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        h = []
        ans = 0
        for c, a in zip(s, nums):
            heapq.heappush(h, -a)
            if c == "1":
                ans -= heapq.heappop(h)
        
        return ans