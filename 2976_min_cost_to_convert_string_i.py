# same pair in original and changed may have different costs, wtf
# other than that, pretty easy
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        d = {}
        for a, b, c in zip(original, changed, cost):
            if a not in d:
                d[a] = {}
            if b not in d[a]:
                d[a][b] = c
            else:
                d[a][b] = min(d[a][b], c)
        m = {}
        for a in d:
            m[a] = {}
            h = [(0, a)]
            while h:
                t, b = heapq.heappop(h)
                if b in m[a]:
                    continue
                m[a][b] = t
                if b in d:
                    for bb in d[b]:
                        if bb not in m[a]:
                            heapq.heappush(h, (t + d[b][bb], bb))

        ans = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            if a not in m:
                return -1
            if b not in m[a]:
                return -1
            ans += m[a][b]
        return ans

# floyd-warshall
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        CONSTRAINTS_MAX = 26000000
        A = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        d = [[CONSTRAINTS_MAX] * 26 for _ in range(26)]
        for a, b, c in zip(original, changed, cost):
            d[A[a]][A[b]] = min(d[A[a]][A[b]], c)
            d[A[a]][A[a]] = 0
            d[A[b]][A[b]] = 0
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        ans = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            if d[A[a]][A[b]] >= CONSTRAINTS_MAX:
                return -1
            ans += d[A[a]][A[b]]
        return ans