# annoying cases
class Solution:
    def countTime(self, time: str) -> int:
        ph = 1
        if time[0] == "?" and time[1] == "?":
            ph = 24
        elif time[0] == "?":
            if time[1] > "3":
                ph = 2
            else:
                ph = 3
        elif time[1] == "?":
            if time[0] == "2":
                ph = 4
            else:
                ph = 10

        pm = 1
        if time[3] == "?":
            pm *= 6
        if time[4] == "?":
            pm *= 10
        
        return ph * pm