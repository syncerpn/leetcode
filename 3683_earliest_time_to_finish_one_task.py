# easy
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] + x[1])
        return sum(tasks[0])