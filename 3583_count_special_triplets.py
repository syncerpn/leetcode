# bisect solution
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        d = {}
        for i, a in enumerate(nums):
            if a not in d:
                d[a] = []
            d[a].append(i)
        
        ans = 0
        for a in d:
            n = len(d[a])
            b = 2 * a
            if a == 0:
                for i in range(1, n-1):
                    ans = (ans + i * (n-1-i)) % MOD
            elif b in d:
                m = len(d[b])
                for i in d[a]:
                    l = bisect.bisect(d[b], i)
                    r = m - l
                    ans = (ans + l * r) % MOD
        
        return ans

# why even need bisect, lol
# just two-pointer
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        d = {}
        for i, a in enumerate(nums):
            if a not in d:
                d[a] = []
            d[a].append(i)
        
        ans = 0
        for a in d:
            n = len(d[a])
            b = 2 * a
            if b in d:
                l, m = 0, len(d[b])
                for i in d[a]:
                    while l < m and d[b][l] < i:
                        l += 1
                    ans = (ans + l * (m - l - (a == b))) % MOD
        
        return ans

# lee's solution
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * n
        count = Counter()
        for i in range(n):
            a = nums[i]
            res[i] = count[a << 1]
            count[a] += 1
        count = Counter()
        for i in range(n)[::-1]:
            a = nums[i]
            res[i] *= count[a << 1]
            count[a] += 1
        return sum(res) % (10 ** 9 + 7)