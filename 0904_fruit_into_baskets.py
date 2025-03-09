# sliding window obviously
# this solution keeps only valid windows
# the length of the longest one is kept in ans
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        d = {}
        ans = 0
        for r, f in enumerate(fruits):
            if f not in d:
                d[f] = 0
            d[f] += 1
            while len(d) > 2:
                fl = fruits[l]
                d[fl] -= 1
                if d[fl] == 0:
                    del d[fl]
                l += 1
            ans = max(ans, r - l + 1)
        return ans

# but it would be much much more brilliant
# by keeping the longest valid window
# that also tells you the answer
# this would save a lot of computations, 2x specifically with leetcode's tests
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        d = {}
        for r, f in enumerate(fruits):
            if f not in d:
                d[f] = 0
            d[f] += 1
            if len(d) > 2:
                fl = fruits[l]
                d[fl] -= 1
                if d[fl] == 0:
                    del d[fl]
                l += 1
        return r - l + 1