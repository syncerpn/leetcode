# lol, not sure why this bit-manip solution
# is even slower than solutions that actually compute the product
# leetcode time measurement is shitty
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = True
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                p = not p
        return 1 if p else -1