# greedy approach O(max_d + nlogn)
# first sort the events by the starting date
# we want to iterate from day 1 to day max_d
# for each day d, plan them in a heapq h by their end dates
# after planning, we can attend one event at a time, greedily the one ends soonest
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        h = []
        i, n = 0, len(events)
        ans = 0
        max_d = max(b for a, b in events)
        for d in range(1, max_d+1):
            while h:
                c = heapq.heappop(h)
                if c >= d:
                    heapq.heappush(h, c)
                    break
            while i < n and events[i][0] == d:
                heapq.heappush(h, events[i][1])
                i += 1
            if h:
                heapq.heappop(h)
                ans += 1
        return ans

# another way, said to be O(nlogn) strictly
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        h = []
        ans = 0
        d = 0
        while events or h:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            ans += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return ans

# think about it in a more easy-to-understand way
# when a day comes, we just plan every available event
# and try to attend them before they close
# and that's it