# just consider each case
class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(":")
        if h[0] == "?" and h[1] == "?":
            h = "23"
        elif h[0] == "?":
            h = "2" + h[1] if int(h[1]) < 4 else "1" + h[1]
        elif h[1] == "?":
            h = h[0] + "9" if int(h[0]) < 2 else "23"
        
        if m[0] == "?" and m[1] == "?":
            m = "59"
        elif m[0] == "?":
            m = "5" + m[1]
        elif m[1] == "?":
            m = m[0] + "9"
        
        return h + ":" + m