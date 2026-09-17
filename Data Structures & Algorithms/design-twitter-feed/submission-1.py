class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = []
        users = set(self.following[userId])
        users.add(userId)
        total_tweets = []

        for user in users:
            total_tweets.extend(self.tweets[user])

        for time, tweet in total_tweets:
            heapq.heappush(newsfeed,(-time, tweet))

        if len(newsfeed) > 10:
            answer = heapq.nsmallest(10,newsfeed)
            result = []
            for time, tweet in answer:
                result.append(tweet)


        else:
            result = []
            answer = heapq.nsmallest(len(newsfeed),newsfeed)
            for time,tweet in answer:
                result.append(tweet)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

        else:
            return None
        
