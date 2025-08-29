# math
# odd of first * even of second + even of first * odd of second
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        no, ne = n - n // 2, n // 2
        mo, me = m - m // 2, m // 2
        return no * me + ne * mo

# compact formula
# odd position of n x m chess board
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n * m // 2