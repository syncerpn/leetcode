# day count needs reference as usual
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ACCDAYS = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        for i in range(1, len(ACCDAYS)):
            ACCDAYS[i] += ACCDAYS[i-1]
        
        def dayth(date):
            m, d = date.split("-")
            return ACCDAYS[int(m)] + int(d)
        
        return max(0, min(dayth(leaveAlice), dayth(leaveBob)) - max(dayth(arriveAlice), dayth(arriveBob)) + 1)