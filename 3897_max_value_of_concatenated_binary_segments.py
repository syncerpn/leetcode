# fairly easy
# prefer all-one segment first
# then come those with more ones
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = 10 ** 9 + 7
        only_one = 0
        P = []
        for o, z in zip(nums1, nums0):
            if z == 0:
                only_one += o
            else:
                P.append((o, z))
        P.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        while only_one:
            ans = ((ans << 1) | 1) % MOD
            only_one -= 1
        for o, z in P:
            for _ in range(o):
                ans = ((ans << 1) | 1) % MOD
            for _ in range(z):
                ans = (ans << 1) % MOD
        return ans

# if you dont care about big numbers
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = 10 ** 9 + 7
        only_one = 0
        P = []
        for o, z in zip(nums1, nums0):
            if z == 0:
                only_one += o
            else:
                P.append((o, z))
        P.sort(key=lambda x: (-x[0], x[1]))
        ans = ((1 << only_one) - 1) % MOD
        for o, z in P:
            v = ((1 << o) - 1) << z
            ans = ((ans << (o + z)) | v) % MOD
        return ans