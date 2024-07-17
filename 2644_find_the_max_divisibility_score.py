# just count
# make it compact
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        score = [[sum([n % d == 0 for n in nums]), -d] for d in divisors]
        _, r = max(score)
        return -r