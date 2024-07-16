# get the list of numbers in diag
# then descending sort and check from beginning
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n == 1:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        n = len(nums)
        d = [nums[i][i] for i in range(n)] + [nums[i][n-1-i] for i in range(n)]
        d.sort(reverse=True)
        for di in d:
            if is_prime(di):
                return di
        return 0

# i was also introduced to sieve algorithm for building up prime memoi
# that helps saving prime checking time