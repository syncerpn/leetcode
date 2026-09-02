# pre-compute sieve of era
# then sliding window
Q = [True] * (100001)
P = []
for a in range(2, 100001):
    if not Q[a]:
        continue
    P.append(a)
    b = a
    while a * b < 100001:
        Q[a * b] = False
        b += 1

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        @functools.cache
        def count_factor(a):
            if Q[a]:
                return tuple([a])
            d = []
            for p in P:
                if p > a:
                    break
                if a % p == 0:
                    while a % p == 0:
                        a //= p
                    d.append(p)
            return tuple(d)

        l = 0
        dd = {}
        ans = 0
        for r, a in enumerate(nums):
            d = count_factor(a)
            for p in d:
                if p not in dd:
                    dd[p] = 0
                dd[p] += 1

            while len(dd) > k:
                b = nums[l]
                d = count_factor(b)
                for p in d:
                    dd[p] -= 1
                    if dd[p] == 0:
                        del dd[p]
                l += 1

            ans = max(ans, r - l + 1)
        return ans