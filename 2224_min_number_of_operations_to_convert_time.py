# try removing the diff
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h, m = current.split(":")
        current = int(h) * 60 + int(m)
        h, m = correct.split(":")
        correct = int(h) * 60 + int(m)
        d = correct - current
        r = 0
        if d >= 60:
            r += d // 60
            d = d % 60
        if d >= 15:
            r += d // 15
            d = d % 15
        if d >= 5:
            r += d // 5
            d = d % 5
        r += d
        return r