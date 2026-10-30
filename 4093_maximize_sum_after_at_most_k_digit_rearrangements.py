# easy
class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        def helper(a):
            D = []
            while a > 0:
                d = a % 10
                a //= 10
                D.append(d)
            D.sort(reverse=True)
            aa = 0
            for d in D:
                aa = aa * 10 + d
            return aa
        ans = sum(nums)
        B = []
        for a in nums:
            aa = helper(a)
            B.append(max(0, aa - a))
        B.sort(reverse=True)
        return ans + sum(B[:k])