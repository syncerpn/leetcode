# simulate it
class Solution:
    def numberOfSteps(self, num: int) -> int:
        r = 0
        while num:
            if num % 2:
                num ^= 1
            else:
                num >>= 1
            r += 1
        return r
