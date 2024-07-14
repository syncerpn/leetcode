# pretty good problem
# this solution can be applied to solve #2176 faster
# the point is, we want to break down each n in nums
# and keep track of gcd of n and k with a hash table
# then iterate the hash table and count with math
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def gcd(n, k):
            while n and k:
                n, k = k, n % k
            return n
        
        gs = {}
        for n in nums:
            g = gcd(n, k)
            if g not in gs:
                gs[g] = 0
            gs[g] += 1
        
        r = 0
        ks = list(gs.keys())
        for i in range(len(ks)):
            ki = ks[i]
            for j in range(i, len(ks)):
                kj = ks[j]
                if (ki * kj) % k == 0:
                    if ki == kj:
                        r += gs[ki] * (gs[ki] - 1) // 2
                    else:
                        r += gs[ki] * gs[kj]
        
        return r