# maybe revisit this sometimes to learn the optimal solution
# dp recursive with functools.cache
class Solution:
    @functools.cache
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        f = n ** 0.5
        k = int(f)
        if k == f:
            return 1
        return 1 + min(self.numSquares(n-i*i) for i in range(1, k+1))

# or how about dp manually
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[1] = 1
        dp[0] = 0
        for k in range(2, n+1):
            r = int(k ** 0.5)
            for i in range(1, r+1):
                dp[k] = min(dp[k], 1+dp[k-i*i])
        return dp[n]

# but this can be solved with maths, lol
# how crazy it is
# better learn some maths
# copied from others
class Solution:
    def numSquares(self, n: int) -> int:

        def CheckTwo(c):                       
            while c%2==0: c//= 2
            while c%5==0: c//= 5
            while c%9==0: c//= 9

            if c%3==0: return False

            if c in (0,1,13,17): return True

            i, j = 0, isqrt(c)

            while i <= j:
                if i*i + j*j == c: return True
                if i*i + j*j < c: i += 1
                if i*i + j*j > c: j -= 1

            return  False


        if n == isqrt(n)**2:return 1                # case k = 1       

        if CheckTwo(n): return 2                    # case k = 2

        while n%4 ==0: n//=4                        # case k = 3  
        if n%8 != 7: return 3 
        
        return 4                                    # case k = 4

# another shorter implementation
class Solution:
    def numSquares(self, n: int) -> int:
        if (int(math.sqrt(n)))**2==n:
            return 1
        while n%4==0:
            n//=4
        if n%8==7:
            return 4
        for i in range(1,int(n**0.5)+1):
            if int(math.sqrt(n-i*i))**2==n-i*i:
                return 2
        return 3

# some solved with bfs
# copied from others
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt