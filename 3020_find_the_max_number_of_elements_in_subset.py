# fairly easy
# can be solved in O(n) as well, where sorting is not needed
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = Counter(nums)
        A = sorted(d.keys())
        m = max(A)
        v = set([1])
        ans = (d[1] - 1) // 2 * 2 + 1
        for a in A:
            if a in v:
                continue
            t = 0
            while a <= m:
                if d[a] >= 2:
                    t += 2
                elif d[a] == 1:
                    t += 1
                    ans = max(ans, t)
                    t = 0
                elif d[a] == 0:
                    t -= 1
                    ans = max(ans, t)
                    t = 0
                v.add(a)
                a *= a
            else:
                t -= 1
                ans = max(ans, t)
        return ans