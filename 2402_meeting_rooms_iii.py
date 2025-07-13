# need to keep track of free rooms, and busy rooms and when they become available
# with heaps
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        h, f = [], list(range(n))
        heapq.heapify(f)

        d = [0] * n
        ans = 0
        for a, b in meetings:
            while h:
                c, i = heapq.heappop(h)
                if c <= a:
                    heapq.heappush(f, i)
                else:
                    heapq.heappush(h, (c, i))
                    break
            if f:
                i = heapq.heappop(f)
                d[i] += 1
                heapq.heappush(h, (b, i))
            else:
                c, i = heapq.heappop(h)
                d[i] += 1
                heapq.heappush(h, (c + b - a, i))
        ans = 0
        m = 0
        for i in range(n):
            if d[i] > m:
                m = d[i]
                ans = i
        return ans