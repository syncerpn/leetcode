class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        D = [Counter(list(word)) for word in words]
        S = [d[min(d.keys())] for d in D]
        
        Q = [Counter(list(word)) for word in queries]
        P = [(d[min(d.keys())], i) for i, d in enumerate(Q)]
        S.sort()
        P.sort()
        m, n = len(S), len(P)
        j = 0
        ans = [0] * n
        for p, i in P:
            while j < m and p >= S[j]:
                j += 1
            ans[i] = m - j
        return ans