# i believe random should work much better
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zeros(n):
            while n:
                if n % 10 == 0:
                    return True
                n //= 10
            return False
        
        while True:
            i = random.randint(1, n-1)
            if not has_zeros(i) and not has_zeros(n-i):
                return [i, n-i]
