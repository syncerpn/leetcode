# easy
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        sh, sm, ss = list(map(int, startTime.split(":")))
        eh, em, es = list(map(int, endTime.split(":")))
        return (eh - sh) * 3600 + (em - sm) * 60 + (es - ss)