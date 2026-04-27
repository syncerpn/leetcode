# a bit of math
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        def group_dist(s):
            m = len(s)
            p = sum(a - s[0] for a in s)
            ans[s[0]] = p
            for i, (a, b) in enumerate(pairwise(s)):
                ans[b] = ans[a] + (i + 1) * (b - a) - (m - i - 1) * (b - a)
        
        d = defaultdict(list)
        for i, a in enumerate(nums):
            d[a].append(i)
        
        for a in d:
            group_dist(d[a])
        return ans