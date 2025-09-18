# fairly easy
# though, again, we may push a lot of garbage into the memory
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.T = []
        self.P = {}
        self.U = {}
        for u, t, p in tasks:
            self.P[t] = p
            self.U[t] = u
            heapq.heappush(self.T, (-p, -t))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.P[taskId] = priority
        self.U[taskId] = userId
        heapq.heappush(self.T, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.P[taskId] = newPriority
        u = self.U[taskId]
        heapq.heappush(self.T, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        del self.P[taskId]
        del self.U[taskId]

    def execTop(self) -> int:
        while self.T:
            pn, tn = heapq.heappop(self.T)
            if -tn in self.P and self.P[-tn] == -pn:
                del self.P[-tn]
                u = self.U[-tn]
                del self.U[-tn]
                return u
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()