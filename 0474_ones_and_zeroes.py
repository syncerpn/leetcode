# greedy did not work
# so dp with table m x n
# that dp[i][j] != -1 checking saved a lot of running time actually
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ss = []
        for s in strs:
            k = len(s)
            t = sum(list(map(int, s)))
            ss.append((k-t, t))
        
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 0
        for a, b in ss:
            for i in range(m-a,-1,-1):
                for j in range(n-b,-1,-1):
                    if dp[i][j] != -1:
                        dp[i+a][j+b] = max(dp[i+a][j+b], dp[i][j] + 1)
        
        return max([max(d) for d in dp])