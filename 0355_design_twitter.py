# heap
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.user_tweets = {}
        self.user_follows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.timestamp += 1
        self.user_tweets[userId].append((-self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.user_tweets:
            heap.extend(self.user_tweets[userId][-10:])
        if userId in self.user_follows:
            for followeeId in self.user_follows[userId]:
                if followeeId in self.user_tweets:
                    heap.extend(self.user_tweets[followeeId][-10:])
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop(heap)[1])
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follows:
            self.user_follows[followerId] = set()
        if followerId != followeeId:
            self.user_follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_follows and followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)