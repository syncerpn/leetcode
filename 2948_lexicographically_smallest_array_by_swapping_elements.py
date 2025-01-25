# with deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s = sorted(nums)
        d = {s[0]: 0}
        p = [deque([s[0]])]
        for a, b in pairwise(s):
            if b - a <= limit:
                d[b] = d[a]
                p[-1].append(b)
            else:
                d[b] = d[a] + 1
                p.append(deque([b]))
        ans = []
        for a in nums:
            ans.append(p[d[a]].popleft())
        return ans

# maybe not need that, just track index and offset of each group
# (and also overwrite nums)
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s = sorted(nums)
        d = {}
        p = []
        for i, a in enumerate(s):
            if i == 0 or a - s[i-1] > limit:
                p.append(i)
            d[a] = len(p) - 1
        
        for i, a in enumerate(nums):
            nums[i] = s[p[d[a]]]
            p[d[a]] += 1
        return nums