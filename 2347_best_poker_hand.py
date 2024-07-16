# easy
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        r = {}
        for i in ranks:
            if i not in r:
                r[i] = 0
            r[i] += 1
        s = set(suits)
        p = False
        if len(s) == 1:
            return "Flush"
        for i in r:
            if r[i] >= 3:
                return "Three of a Kind"
            elif r[i] == 2:
                p = True
        
        return "Pair" if p else "High Card"