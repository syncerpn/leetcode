# use this solution, which is computation-based
# otherwise, just use lib
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        DATES = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        MONTHS = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
        c = 0
        for i in range(1971, year):
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                c += 2
            else:
                c += 1
        
        for i in range(month-1):
            c += MONTHS[i]
            if i == 1 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                c += 1
        
        c += day
        return DATES[c % 7]