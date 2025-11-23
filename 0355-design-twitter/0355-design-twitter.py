class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = deque()
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        r = []
        followees = self.following.get(userId, set())
        for post_user_id, tweet_id in reversed(self.posts):
            if len(r) == 10:
                break
            if post_user_id == userId or post_user_id in followees:
                r.append(tweet_id)
        return r
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)