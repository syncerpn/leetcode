# solve with dp, beautiful solution
# to get to nth step, we either take one step from n-1 or two steps from n-2
# so it simplifies down to fibonacci
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# this is my own solution, using math
# but seems quite bad
class Solution:
    FCACHE = {}
    def climbStairs(self, n: int) -> int:
        def factorial(i):
            if i in Solution.FCACHE:
                return Solution.FCACHE[i]

            if i < 2:
                Solution.FCACHE[i] = 1
                return Solution.FCACHE[i]
            
            Solution.FCACHE[i] = i * factorial(i-1)
            return Solution.FCACHE[i]

        r = 0
        #i denotes number of 2
        #n-i*2 denotes number of 1
        for i in range(n//2+1):
            j = n - i * 2
            r += factorial(i+j) // (factorial(i) * factorial(j))
        
        return r