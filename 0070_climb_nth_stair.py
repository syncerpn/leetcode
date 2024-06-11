#1. solve with dp, beautiful solution
#2. to get to nth step, we either take one step from n-1 or two steps from n-2
#3. so it simplifies down to fibonacci
def solve(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


#1. this is my own solution, using math
#2. but seems quite bad
FCACHE = {}
def solve2(self, n: int) -> int:
    def factorial(i):
        if i in FCACHE:
            return FCACHE[i]

        if i < 2:
            FCACHE[i] = 1
            return FCACHE[i]
        
        FCACHE[i] = i * factorial(i-1)
        return FCACHE[i]

    r = 0
    #i denotes number of 2
    #n-i*2 denotes number of 1
    for i in range(n//2+1):
        j = n - i * 2
        r += factorial(i+j) // (factorial(i) * factorial(j))
    
    return r