# actually this is a tree, lol, so union-find below is kinda overreact
# my solution (overreacted one)
# union find and 0/1 chain
# fairly easy to think of an algorithm
# but implementation is quite difficult
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        f = [i for i in range(n)]

        def find(x):
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        
        def union(x, y):
            f[find(x)] = find(y)

        for a, b in edges:
            union(a, b)
        
        d, g ,s = {}, {}, {}
        for a in range(n):
            b = find(a)
            x = nums[a] ^ k
            if b not in d:
                d[b] = abs(nums[a] - x)
                g[b] = True if nums[a] < x else False
                s[b] = max(nums[a], x)
            else:
                d[b] = min(d[b], abs(nums[a] - x))
                g[b] = g[b] ^ (True if nums[a] < x else False)
                s[b] = s[b] + max(nums[a], x)

        ans = sum([s[b] - d[b] if g[b] else s[b] for b in s])
        return ans

# again, with a tree, no need for union-find, just do this
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        d, g, s = float("inf"), False, 0
        for a in nums:
            x = a ^ k
            d = min(d, abs(a - x))
            g = g ^ (True if a < x else False)
            s = s + max(a, x)

        return s - d if g else s
