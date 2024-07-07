# also very simple
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        c = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                c += 1
        
        return c