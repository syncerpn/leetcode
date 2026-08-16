# easy
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        d = Counter(planks)
        f = Counter(planks)
        v = set()
        for a in d:
            for b in d:
                if b in v:
                    continue
                if a == b:
                    f[a + b] += d[a] // 2
                else:
                    f[a + b] += min(d[a], d[b])
            
            v.add(a)
        
        return max(list(f.values()))