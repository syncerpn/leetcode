# need revisit
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def helper(x):
            if x == 0:
                return 0
            
            k = 0
            c = 1
            while c * 2 <= x:
                c *= 2
                k += 1

            return 2 ** (k + 1) - 1 - helper(x ^ c)
        
        return helper(n)