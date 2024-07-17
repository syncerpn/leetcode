# zip and do it in a single pass
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        d = 0
        k1, k2 = 0, 0
        for n1, n2 in zip(player1, player2):
            d += n1 - n2
            if k1 > 0:
                d += n1
                k1 -= 1
            if k2 > 0:
                d -= n2
                k2 -= 1
            if n1 == 10:
                k1 = 2
            if n2 == 10:
                k2 = 2
        return 0 if d == 0 else (1 if d > 0 else 2)