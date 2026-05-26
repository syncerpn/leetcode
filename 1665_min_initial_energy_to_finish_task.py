# greedy
# basically, when doing the tasks, we want to have more energy after doing each task
# and also the least amount of unused energy in the end
# so we can sort the tasks by the difference between actual and required energy
# since the difference is negative (because actual <= required)
# more negative first
tclass Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: (t[0] - t[1]))
        ans = 0
        e = 0
        for c, r in tasks:
            if e < r:
                ans += r - e
                e = r
            e -= c
        return ans