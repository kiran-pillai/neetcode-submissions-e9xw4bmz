import heapq
from collections import deque, defaultdict
import numpy as np
from itertools import islice

class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follower_map = defaultdict(set)
        self.timer = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.posts[user_id].append({"tweet_id":tweet_id, "timer":self.timer})
        self.timer+=1

        

    def getNewsFeed(self, user_id: int) -> List[int]:
        user_ids = {user_id}
        user_ids.update(self.follower_map[user_id])
        all_posts = []
        for user in user_ids:
            all_posts.extend(self.posts[user])
        all_posts.sort(key = lambda post: post["timer"], reverse = True)
        return [post["tweet_id"] for post in all_posts[:10]]


    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follower_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follower_map[follower_id]:
            self.follower_map[follower_id].remove(followee_id)
        