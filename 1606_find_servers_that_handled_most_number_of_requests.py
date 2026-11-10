# sortedlist is powerful
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        s = []
        f = SortedList(range(k))
        b = [0] * k
        for i, (a, l) in enumerate(zip(arrival, load)):
            i %= k
            while s and s[0][0] <= a:
                _, j = heapq.heappop(s)
                f.add(j)
            
            if not f:
                continue
            jj = bisect.bisect_left(f, i)
            if jj == len(f):
                jj = 0
            j = f[jj]
            heapq.heappush(s, (a + l, j))
            b[j] += 1
            f.remove(j)

        m = max(b)
        ans = []
        for i in range(k):
            if b[i] == m:
                ans.append(i)
        return ans

# can also be solved with 2 heaps
# with a wrap around trick to pop out the correct server id
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        heapq.heapify(available)

        busy = []
        count = [0] * k

        for i, start in enumerate(arrival):

            # Release completed servers
            while busy and busy[0][0] <= start:
                end_time, server = heapq.heappop(busy)

                virtual = i + (server - i) % k
                heapq.heappush(available, virtual)

            # Assign the next available server
            if available:
                server = heapq.heappop(available) % k

                heapq.heappush(busy, (start + load[i], server))
                count[server] += 1

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]