# just follow the rule
class Solution:
    def checkRecord(self, s: str) -> bool:
        c_late = 0
        c_absent = 0
        for c in s:
            if c == "L":
                c_late += 1
                if c_late >= 3:
                    return False
            else:
                c_late = 0
                if c == "A":
                    c_absent += 1
                    if c_absent >= 2:
                        return False
        
        return True