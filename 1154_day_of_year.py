# be careful with leap year condition
class Solution:
    def dayOfYear(self, date: str) -> int:
        MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = list(map(int, date.split("-")))
        t = d + ((y % 4 == 0 and not y % 100 == 0) or (y % 400 == 0)) * (m > 2)
        for i in range(m-1):
            t += MONTHS[i]
        return t