# counter and greedy removal
class Solution:
    def minDeletions(self, s: str) -> int:
        d = Counter(list(s))
        V = sorted(list(d.values()))
        n = len(V)
        ans = 0
        for i in range(n-2, -1, -1):
            if V[i] >= V[i+1]:
                p = V[i]
                V[i] = max(0, V[i+1] - 1)
                ans += p - V[i]
        return ans