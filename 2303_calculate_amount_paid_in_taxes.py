# simulate it in O(n)
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        m = 0
        t = 0
        for u, p in brackets:
            t += (min(u, income) - m) * p / 100
            m = u
            if m >= income:
                break
        
        return t