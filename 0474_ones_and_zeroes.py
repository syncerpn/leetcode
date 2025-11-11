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

# knapsack dp
# another solution that store only possible combs
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        dp = {(0,0): 0}
        for s in strs:
            z = s.count("0")
            o = s.count("1")
            dp_keys = list(dp.keys())
            dpn = {i: dp[i] for i in dp}
            for mi, ni in dp_keys:
                mzi = mi + z
                noi = ni + o
                if mzi > m or noi > n:
                    continue
                if (mzi, noi) not in dpn:
                    dpn[(mzi, noi)] = 0
                dpn[(mzi, noi)] = max(dpn[(mzi, noi)], dp[(mi, ni)] + 1)
            dp = dpn
        return max(dp[i] for i in dp)
# the following solution does not work because of overwriting previous state, causing duplication
# and leading to invalidly high answer:
#
# if (mi+zi, ni+oi) not in dp:
#     dp[(mi+zi, ni+oi)] = 0
# dp[(mi+zi, ni+oi)] = max(dp[(mi+zi, ni+oi)], dp[(mi, ni)] + 1)
#
# we need dpn (next state) to avoid this