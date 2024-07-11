# simple again
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        k = 0
        if ruleKey == "color":
            k = 1
        elif ruleKey == "name":
            k = 2
        
        c = 0
        for item in items:
            if item[k] == ruleValue:
                c += 1
        return c