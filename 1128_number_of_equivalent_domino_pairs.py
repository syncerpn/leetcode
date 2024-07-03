# just count with math formula
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            if a * 10 + b not in d:
                d[a * 10 + b] = 0
            d[a * 10 + b] += 1
        
        c = 0
        for k in d:
            c += d[k] * (d[k] - 1) // 2
        return c