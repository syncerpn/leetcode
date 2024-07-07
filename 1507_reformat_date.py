# just lookup and build
class Solution:
    def reformatDate(self, date: str) -> str:
        MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split(" ")
        dd = d[:-2]
        mm = MONTHS.index(m) + 1
        return f"{y}-{mm:02}-{int(dd):02}"