class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        n = len(arrivals)
        f = [False] * n
        d = {}
        for i, a in enumerate(arrivals):
            if a not in d:
                d[a] = 0
            d[a] += 1
            if i >= w:
                if not f[i-w]:
                    d[arrivals[i-w]] -= 1
            if d[a] > m:
                f[i] = True
                d[a] -= 1
        return sum(f)
