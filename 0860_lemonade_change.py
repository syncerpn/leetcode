# greedy change payment
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills_5 = 0
        bills_10 = 0
        for b in bills:
            if b == 10:
                bills_10 += 1
                if bills_5 <= 0:
                    return False
                bills_5 -= 1
            elif b == 20:
                if bills_10 > 0:
                    bills_10 -= 1
                    if bills_5 <= 0:
                        return False
                    bills_5 -= 1
                else:
                    if bills_5 < 3:
                        return False
                    bills_5 -= 3
            else:
                bills_5 += 1
                
        return True