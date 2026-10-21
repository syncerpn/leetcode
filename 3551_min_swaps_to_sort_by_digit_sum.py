# mismatch chain detection
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(a):
            ans = 0
            while a > 0:
                ans += a % 10
                a //= 10
            return ans
        n = len(nums)
        A = sorted(list(range(n)), key=lambda i: (digit_sum(nums[i]), nums[i]))
        f = [False] * n
        ans = 0
        for i, a in enumerate(A):
            if f[a]:
                continue
            p = 1
            f[i] = True
            while not f[a]:
                f[a] = True
                a = A[a]
                p += 1
            ans += p - 1
        return ans