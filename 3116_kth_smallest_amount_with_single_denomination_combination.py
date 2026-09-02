# inclusion-exclusion principle
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def check(m):
            tot = 0
            for x in range(1, len(coins) + 1):
                for c in combinations(coins, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * coins[0] + 1), True, lo=1, key=check)

# remove some cases where denom of one is multiple of earlier denom
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
    
        A = []
        for x in coins:
            if all(x % c for c in A):
                A.append(x)
    
        def check(m):
            tot = 0
            for x in range(1, len(A) + 1):
                for c in combinations(A, x):
                    tot += m // lcm(*c) * pow(-1, x + 1)
            return tot >= k
    
        return bisect_left(range(k * A[0] + 1), True, lo=1, key=check)

# gosher? need revisit
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        A = []
        for c in coins:
            if all(c % x for x in A):
                A.append(c)

        n = len(A)

        def check(mid):
            tot = 0
            for i in range(1, n + 1):
                q = (1 << i) - 1
                lim = 1 << n
                sgn = ((i & 1) << 1) - 1

                while q < lim:
                    x = 1
                    for j in range(n):
                        if (q >> j) & 1:
                            x = lcm(x, A[j])

                    tot += (mid // x) * sgn

                    c = q & -q
                    r = q + c
                    q = (((r ^ q) >> 2) // c) | r
            return tot >= k

        return bisect_left(range(A[0] * k + 1), True, lo=k, key=check)