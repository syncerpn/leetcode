# i was surprised O(n2) works
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        ps = list(range(n))
        ps.sort(key=lambda p: times[p])
        h = []
        v = set()

        for i, p in enumerate(ps):
            a, l = times[p]
            while h and h[0][0] <= a:
                _, j = heapq.heappop(h)
                v.discard(j)

            j = 0
            while j in v:
                j += 1

            heapq.heappush(h, (l, j))
            v.add(j)
            if p == targetFriend:
                break
        
        return j

# much faster if we save the available chair list as a heap too
# then we can pop to get the smallest available one in no time
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        ps = list(range(n))
        ps.sort(key=lambda p: times[p])
        h, s = [], list(range(n))

        for i, p in enumerate(ps):
            a, l = times[p]
            while h and h[0][0] <= a:
                _, j = heapq.heappop(h)
                heapq.heappush(s, j)
            
            j = heapq.heappop(s)
            heapq.heappush(h, (l, j))
            if p == targetFriend:
                break
        
        return j