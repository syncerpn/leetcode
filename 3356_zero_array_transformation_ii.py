# pretty much similar to the previous one #3355
# just use binary search to find the minimum k
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def is_valid(k):
            changes = [0] * n
            for l, r, v in queries[:k]:
                changes[l] += v
                if r + 1 < n:
                    changes[r+1] -= v
        
            p = 0
            for a, b in zip(nums, changes):
                p += b
                if p < a:
                    print(p, k, a)
                    return False
            return True
        
        l = 0
        r = len(queries)
        ans = -1
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans

# but this is linear runtime optimal solution
# which is just super beautiful
# we greedily checking each query, recording change in line-sweep style
# while also accumulate (prefix-sum) of all changes that happen to the current index of nums
# if those changes, meaning the total val to be decreased at the current index, are bigger than the value at the current index itself
# it can be reduced to zero
# and then we check the next index in nums
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        d = [0] * (n + 1)
        s, k = 0, 0
        for i, a in enumerate(nums):
            while s + d[i] < a:
                if k == m:
                    return -1
                l, r, v = queries[k]
                k += 1

                if r < i:
                    continue
                d[max(l, i)] += v
                d[r+1] -= v
            
            s += d[i]
        
        return k