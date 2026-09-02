# easy
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        v = set()
        b = set()
        p = None
        ans = 0
        for a in nums:
            if a != p:
                if a not in v and a not in b:
                    v.add(a)
                else:
                    b.add(a)
            p = a
        return len(v) - len(b)