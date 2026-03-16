# just do it
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        s = []
        m = -inf
        for a in nums:
            if a >= m:
                m = a
                s.append(m)
            else:
                s.append(math.gcd(m, a))
        
        s.sort()
        ans = 0
        for i in range(len(s) // 2):
            ans += math.gcd(s[i], s[~i])
        return ans