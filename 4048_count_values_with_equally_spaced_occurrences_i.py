# easy
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        f = set()
        for i, a in enumerate(nums):
            if a not in d:
                d[a] = []
            d[a].append(i)
            if len(d[a]) == 3 and d[a][2] + d[a][0] == 2 * d[a][1]:
                f.add(a)
            elif len(d[a]) > 3:
                f.discard(a)
        return len(f)
