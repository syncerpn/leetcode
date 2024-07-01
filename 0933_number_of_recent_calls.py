# just queue
# only need to keep track of those within 3000ms before the ping moment
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q:
            if self.q[0] >= t - 3000:
                break
            self.q.popleft()
            
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)