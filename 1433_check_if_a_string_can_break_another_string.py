# easy, just sort
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        logic = 0
        for a, b in zip(s1, s2):
            if a > b:
                if logic == -1:
                    return False
                logic = 1
            elif a < b:
                if logic == 1:
                    return False
                logic = -1
        return True