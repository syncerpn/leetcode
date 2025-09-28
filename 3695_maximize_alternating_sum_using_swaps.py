# union-find
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        r = [0] * n
        p = list(range(n))

        def find(a):
            pa = p[a]
            if pa != a:
                return find(pa)
            return pa
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if r[pa] < r[pb]:
                    p[pa] = pb
                elif r[pa] > r[pb]:
                    p[pb] = pa
                else:
                    p[pb] = pa
                    r[pa] += 1
        
        for a, b in swaps:
            union(a, b)
        d = {}
        for a in range(n):
            pa = find(a)
            if pa not in d:
                d[pa] = [0, []]
            d[pa][0] += a % 2
            d[pa][1].append(nums[a])
        
        ans = 0
        for pa in d:
            k, v = d[pa]
            v.sort()
            for i, a in enumerate(v):
                if i < k:
                    ans -= a
                else:
                    ans += a
        return ans
