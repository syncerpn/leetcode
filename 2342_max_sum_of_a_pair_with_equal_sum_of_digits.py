# optimal single-pass
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        ans = -1
        for a in nums:
            b = a
            s = 0
            while b:
                s += b % 10
                b //= 10:

            if s not in d:
                d[s] = [0, a]
            else:
                if a > d[s][1]
                    d[s][0], d[s][1] = d[s][1], a
                    ans = max(ans, sum(d[s]))
                elif a > d[s][0]:
                    d[s][0] = a
                    ans = max(ans, sum(d[s]))
        return ans