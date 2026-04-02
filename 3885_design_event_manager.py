# easy
# late garbage collector
# also need to handle case where duplicate entries are added to the queue
class EventManager:

    def __init__(self, events: list[list[int]]):
        self.h = []
        self.d = {}
        for i, p in events:
            self.d[i] = p
            heapq.heappush(self.h, (-p, i))


    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.d[eventId] = newPriority
        heapq.heappush(self.h, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.h:
            pn, i = heapq.heappop(self.h)
            p = -pn
            if i in self.d and self.d[i] == p:
                del self.d[i]
                return i
        return -1
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()