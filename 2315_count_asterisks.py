# add to stack when out of bars
class Solution:
    def countAsterisks(self, s: str) -> int:
        r = ""
        b = False
        for c in s:
            if c == "|":
                b = ~b
            elif not b:
                r += c
        
        return r.count("*")