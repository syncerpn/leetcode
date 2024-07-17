# annoying problem though
class Solution:
    def findLatestTime(self, s: str) -> str:
        ph = s[0:2]
        if s[0] == "?" and s[1] == "?":
            ph = "11"
        elif s[0] == "?":
            if s[1] > "1":
                ph = "0" + s[1]
            else:
                ph = "1" + s[1]
        elif s[1] == "?":
            if s[0] == "0":
                ph = "09"
            else:
                ph = "11"

        m1 = s[3]
        m2 = s[4]
        if s[3] == "?":
            m1 = "5"
        if s[4] == "?":
            m2 = "9"
        
        return ph + ":" + m1 + m2
        