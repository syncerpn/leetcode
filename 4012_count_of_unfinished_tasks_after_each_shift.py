# python handles big nums well
# we can use prefix sum
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        for i in range(1, n):
            tasks[i] += tasks[i-1]
        ans = []
        p = 0
        for s in shifts:
            p += s
            i = bisect.bisect(tasks, p)
            ans.append(n - i)
            if i == n:
                p = 0
        return ans