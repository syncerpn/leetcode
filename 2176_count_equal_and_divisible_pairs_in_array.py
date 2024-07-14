# maybe this O(n2) is fair
# some suggested using gcd for a (Onsqrtn)
# but it seems not so much better
# please refer to #2183 for more details
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = []
            d[n].append(i)
        
        r = 0
        for n in d:
            if len(d[n]) < 2:
                continue
            for i in range(len(d[n])):
                for j in range(i+1, len(d[n])):
                    if d[n][i] * d[n][j] % k == 0:
                        r += 1
        
        return r