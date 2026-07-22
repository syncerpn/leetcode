# binary search + dijkstra
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        r = 0
        g = defaultdict(list)
        for a, b, c in edges:
            g[a].append((b, c))
            r = max(r, c)

        def is_valid(m):
            h = []
            heapq.heappush(h, (0, 0))
            v = defaultdict(int)

            while h:
                s, a = heapq.heappop(h)
                if a == n - 1:
                    return True

                if a in v and v[a] <= s:
                    continue
                v[a] = s

                for b, c in g[a]:
                    if s + c > k:
                        continue
                    if not online[b]:
                        continue
                    if c < m:
                        continue
                    heapq.heappush(h, (s + c, b))

            return False

        l = -1

        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                l = m + 1
            else:
                r = m - 1
        return r if r >= 0 else -1