# any better than O(n^2)??
class Solution:
    def getLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for k in range(n):
            d = {}
            f = {}
            for i in range(k, n):
                a = nums[i]
                if a not in d:
                    d[a] = 1
                    if 1 not in f:
                        f[1] = 0
                    f[1] += 1

                else:
                    b = d[a]
                    f[b] -= 1
                    if f[b] == 0:
                        del f[b]
                    
                    d[a] += 1
                    b += 1
                    if b not in f:
                        f[b] = 0
                    f[b] += 1
                
                if len(f) == 1 and f[list(f.keys())[0]] == 1:
                    ans = max(ans, i - k + 1)
                elif len(f) == 2:
                    p, q = list(f.keys())
                    p, q = min(p, q), max(p, q)
                    if q == 2 * p:
                        ans = max(ans, i - k + 1)
        return ans