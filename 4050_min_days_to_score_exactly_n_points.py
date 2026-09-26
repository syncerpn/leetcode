# bfs
class Solution:
    def minDays(self, n: int) -> int:
        dp = [(1, 2)]
        f = [False] * (n + 1)
        t = 1
        while dp:
            dp_next = []
            for s, k in dp:
                if s == n:
                    return t
                if s > n:
                    continue
                if s + k <= n:
                    dp_next.append([s + k, k + 1])
                if k > 1 and not f[s]:
                    dp_next.append([s, 1])
                    f[s] = True
            dp = dp_next
            t += 1
        return -1

# dp O(n)
class Solution:
    def minDays(self, n: int) -> int:
        dp = [0] + [inf] * n
        v = k = 1
        while v <= n:
            dp[v] = k
            for i in range(v + 1, min(n, v + v) + 1):
                dp[i] = min(dp[i], dp[i - v] + k + 1)
            k += 1
            v += k
        return dp[n]