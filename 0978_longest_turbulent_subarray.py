# greedy
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        f = 0
        m = 1
        for a, b in pairwise(arr):
            if b > a:
                if f == -1 or f == 0:
                    m += 1
                else:
                    m = 2
                f = 1
            elif b < a:
                if f == 1 or f == 0:
                    m += 1
                else:
                    m = 2
                f = -1
            else:
                m = 1
                f = 0
            ans = max(ans, m)
        return ans