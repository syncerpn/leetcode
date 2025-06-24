# easy
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def is_prime(a):
            if a < 2:
                return False
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    return False
            return True
        d = Counter(nums)
        for a in d:
            if is_prime(d[a]):
                return True
        return False