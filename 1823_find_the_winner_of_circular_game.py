# this one is josephus problem
# simulate it with array is quite trivial
# even better with python array
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = list(range(1, n+1))
        i = k-1
        for _ in range(n-1):
            del q[i]
            i = (i - 1 + k) % len(q)
        return q[0]

# or recursive
# each recursion assume starting point at k - 1 (with mod n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (self.findTheWinner(n - 1, k) + k - 1) % n + 1

# O(1) space with iterative
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        r = 1
        for i in range(2, n+1):
            r = (r + (k - 1)) % i + 1
        return r