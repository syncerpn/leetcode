# easy
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        return sum(a * d[a] for a in d if d[a] % k == 0)