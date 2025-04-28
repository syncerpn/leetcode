# bfs
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(conversions) + 1
        d = {}
        for s, t, f in conversions:
            if s not in d:
                d[s] = {}
            d[s][t] = f
        
        ans = [1] * n
        v = set([0])
        while v:
            v_next = set()
            for s in v:
                if s not in d:
                    continue
                for t in d[s]:
                    ans[t] = (ans[s] * d[s][t]) % MOD
                    if t in d:
                        v_next.add(t)
            v = v_next
        
        return ans
