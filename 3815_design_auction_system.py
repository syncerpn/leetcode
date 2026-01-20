# add transaction id, or tid
class AuctionSystem:

    def __init__(self):
        self.items = {}
        self.users = {}
        self.tid = 0

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.items:
            self.items[itemId] = []
        heapq.heappush(self.items[itemId], (-bidAmount, -userId, self.tid))
        if userId not in self.users:
            self.users[userId] = {}
        self.users[userId][itemId] = self.tid
        self.tid += 1

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        heapq.heappush(self.items[itemId], (-newAmount, -userId, self.tid))
        if userId not in self.users:
            self.users[userId] = {}
        self.users[userId][itemId] = self.tid
        self.tid += 1

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.users[userId][itemId]

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.items:
            return -1
        while self.items[itemId]:
            na, nu, tid = heapq.heappop(self.items[itemId])
            a = -na
            u = -nu
            if itemId in self.users[u] and self.users[u][itemId] == tid:
                heapq.heappush(self.items[itemId], (na, nu, tid))
                return u
        
        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)

# maybe we dont need tid
# just use amount as tid, lol
class AuctionSystem:

    def __init__(self):
        self.items = {}
        self.users = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if itemId not in self.items:
            self.items[itemId] = []
        heapq.heappush(self.items[itemId], (-bidAmount, -userId))
        if userId not in self.users:
            self.users[userId] = {}
        self.users[userId][itemId] = bidAmount

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        heapq.heappush(self.items[itemId], (-newAmount, -userId))
        if userId not in self.users:
            self.users[userId] = {}
        self.users[userId][itemId] = newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.users[userId][itemId]

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.items:
            return -1
        while self.items[itemId]:
            na, nu = heapq.heappop(self.items[itemId])
            a = -na
            u = -nu
            if itemId in self.users[u] and self.users[u][itemId] == a:
                heapq.heappush(self.items[itemId], (na, nu))
                return u
        
        return -1


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)