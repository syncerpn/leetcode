# each op can make any num divisible by 3
# so just count those are not divisible already
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum([1 for n in nums if n % 3])