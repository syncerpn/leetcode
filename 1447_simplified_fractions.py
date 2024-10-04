# use gcd to check simplified fractions
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)

        ans = []
        for d in range(2, n+1):
            for k in range(1, d):
                if gcd(d, k) == 1:
                    ans.append(f"{k}/{d}")
        
        return ans