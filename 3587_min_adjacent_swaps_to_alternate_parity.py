# move them to the target indices
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        s = []
        for i, a in enumerate(nums):
            if a % 2:
                s.append(i)
        d = 2 * len(s) - len(nums)
        if abs(d) > 1:
            return -1
        ans = float(inf)
        if d == 1 or d == 0:
            k, t = 0, 0
            for i in s:
                k += abs(i - t)
                t += 2
            ans = min(ans, k)
        if d == -1 or d == 0:
            k, t = 0, 1
            for i in s:
                k += abs(i - t)
                t += 2
            ans = min(ans, k)
        return ans