# also easy with binary search
class ExamTracker:

    def __init__(self):
        self.q = [(0, 0)]

    def record(self, time: int, score: int) -> None:
        _, s = self.q[-1]
        self.q.append((time, s + score))

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect.bisect(self.q, (startTime, 0))
        r = bisect.bisect(self.q, (endTime+1, 0))
        _, sl = self.q[l-1]
        _, sr = self.q[r-1]
        return sr - sl
        


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)