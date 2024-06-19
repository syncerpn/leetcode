# represent graph with dict should be fine
# simply count and check the conditions
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        trust_d = set()
        trusted_d = {}
        for a, b in trust:
            trust_d.add(a)
            if b not in trusted_d:
                trusted_d[b] = 0
            trusted_d[b] += 1

        qualified = -1
        for k in trusted_d:
            if k not in trust_d and trusted_d[k] == n-1:
                if qualified == -1:
                    qualified = k
                else:
                    return -1
        
        return qualified
        