# guessing works lol
# because the constraints seem very high while exhausting all possible triplets wont work
# there must be a trick
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        x = 0
        for n in nums:
            x ^= n
        return x