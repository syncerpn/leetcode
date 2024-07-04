# i actually tried to compute it manually
# lol
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def dayOfYear(date: str) -> int:
            MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            y, m, d = list(map(int, date.split("-")))
            t = d + ((y % 4 == 0 and not y % 100 == 0) or (y % 400 == 0)) * (m > 2)
            for i in range(m-1):
                t += MONTHS[i]
            return t
        
        t1 = dayOfYear(date1)
        t2 = dayOfYear(date2)
        y1, m1, d1 = list(map(int, date1.split("-")))
        y2, m2, d2 = list(map(int, date2.split("-")))
        for i in range(1971, y1):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                t1 += 1
            t1 += 365

        for i in range(1971, y2):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                t2 += 1
            t2 += 365
        
        return abs(t1 - t2)