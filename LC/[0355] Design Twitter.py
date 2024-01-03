from collections import defaultdict


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)  # user_id2(timestamp, tweet_id)
        self.friends = defaultdict(set)  # user_id2set_followee_id
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ts += 1
        self.tweets[userId].append((self.ts, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        if userId not in self.friends[userId]:
            self.friends[userId].add(userId)
        for ii in self.friends[userId]:
            for post in self.tweets[ii]:
                if len(news) < 10:
                    heappush(news, post)
                else:
                    if post[0] <= news[0][0]:
                        continue
                    heappushpop(news, post)

        news.sort(reverse=True)
        return [post for ts, post in news]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.friends[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.friends[followerId] and followerId != followeeId:
            self.friends[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
