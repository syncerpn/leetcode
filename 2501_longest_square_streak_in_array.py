# sorting is pretty straightforward
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        d = {}
        ans = -1
        for n in nums:
            if n * n not in d:
                d[n] = 1
            else:
                d[n] = d[n*n] + 1
                ans = max(ans, d[n])
        return ans

# but maybe union-find is more efficient O(n)
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = -1
        while nums:
            n = nums.pop()
            l, r, k = n, n, 1
            while r * r in nums:
                r = r * r
                nums.discard(r)
                k += 1
            while int(l ** 0.5) ** 2 == l:
                l = int(l ** 0.5)
                if l in nums:
                    nums.discard(l)
                    k += 1
                else:
                    break
            ans = max(ans, k)
        return ans if ans > 1 else -1