# just iterate and check
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right+1):
            n = i
            while n > 0:
                d = n % 10
                if d == 0:
                    break
                n //= 10
                if i % d != 0:
                    break
            else:
                r.append(i)

        return r