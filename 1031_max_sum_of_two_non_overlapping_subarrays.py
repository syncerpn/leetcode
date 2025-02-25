# brute force lol
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        f = []
        p = 0
        for i, a in enumerate(nums):
            if i >= firstLen:
                f.append(p)
                p -= nums[i-firstLen]
            p += a
        f.append(p)
        
        s = []
        p = 0
        for i, a in enumerate(nums):
            if i >= secondLen:
                s.append(p)
                p -= nums[i-secondLen]
            p += a
        s.append(p)

        n = len(nums)
        ans = 0
        for i in range(n-firstLen+1):
            for j in range(n-secondLen+1):
                if i + firstLen <= j or j + secondLen <= i:
                    ans = max(ans, f[i] + s[j])
        return ans

# dp, two separate cases: first before second and second before first
# somehow similar to stock selling (twice) problem
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # do a CDF so that range sum can easily be calculated
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        res, fmax, smax = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]

        # window  | --- L --- | --- M --- |
        for i in range(firstLen + secondLen, len(nums)):
            fmax = max(fmax, nums[i - secondLen] - nums[i - firstLen - secondLen])
            res = max(res, fmax + nums[i] - nums[i - secondLen])

        # window  | --- M --- | --- L --- |
        for i in range(firstLen + secondLen, len(nums)):
            smax = max(smax, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, smax + nums[i] - nums[i - firstLen])

        return res
