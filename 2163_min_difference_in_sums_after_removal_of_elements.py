# the power of think different
# we will find the index i that is the optimal partitioning index
# where (sum of the n lowest numbers upto i) - (sum of n highest numbers from i to the end)
# is minimized
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        h, s = [], 0
        for i in range(n):
            heapq.heappush(h, (-nums[i], i))
            s += nums[i]
        l = [s]
        
        for i in range(n, 2*n):
            if -nums[i] > h[0][0]:
                heapq.heappush(h, (-nums[i], i))
                a, j = heapq.heappop(h)
                s += a + nums[i]
            l.append(s)

        h, s = [], 0
        for i in range(2*n, 3*n):
            heapq.heappush(h, (nums[i], i))
            s += nums[i]
        
        r = [s]
        for i in range(2*n-1, n-1, -1):
            if nums[i] > h[0][0]:
                heapq.heappush(h, (nums[i], i))
                a, j = heapq.heappop(h)
                s = s - a + nums[i]
            r.append(s)

        return min(l[i] - r[~i] for i in range(n+1))