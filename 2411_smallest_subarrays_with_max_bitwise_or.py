# my initial solution with sliding window
# keep track of each bit position for un-or operation
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def check(d, s):
            return all(not ((di > 0) ^ si) for di, si in zip(d, s))

        n = len(nums)
        p, s = 0, [[False] * 32 for _ in range(n)]
        for i in range(n):
            p |= nums[~i]
            j, q = 0, p
            while q > 0:
                s[~i][j] = (q & 1) == 1
                q >>= 1
                j += 1

        d = [0] * 32
        ans = []
        k = 0
        for i in range(n):
            while not check(d, s[i]):
                a = nums[k]
                for j in range(32):
                    d[j] += a & 1
                    a >>= 1
                k += 1
            ans.append(max(1, k-i))

            a = nums[i]
            for j in range(32):
                d[j] -= a & 1
                a >>= 1
        return ans

# maybe, how about going backward instead
# and keeping track of the last index bit position is set?
# turns out, we dont even need to precompute max or result
# just try to make sure all the possible set-bits are set
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [0] * 32
        n = len(nums)
        ans = [0] * n

        for i in range(n-1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    last[j] = i
            ans[i] = max(1, max(last) - i + 1)
        
        return ans

# further improve for fast actual run-time
# but modify nums in the procedure
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            a = nums[i]
            j = i - 1
            while j >= 0 and nums[j] | a != nums[j]:
                ans[j] = i - j + 1
                nums[j] |= a
                j -= 1
        return ans