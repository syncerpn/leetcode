# edge cases might make you crazy lol
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        nums.append(0)
        f = True
        e = False
        l, r, p = 0, 0, 0
        for a, b in pairwise(nums):
            if f:
                if a < b:
                    l += a
                else:
                    if a == b:
                        e = True
                    f = False
                    p = a
            else:
                if a <= b:
                    return -1
                else:
                    r += a
        if e:
            return abs(l + p - r)
        return min(abs(l + p - r), abs(l - p - r))