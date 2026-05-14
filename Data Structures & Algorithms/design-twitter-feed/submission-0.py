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
        user_ids = [user_id]
        for follower, followees in self.follower_map.items():
            if follower == user_id:
                user_ids.extend(followees)
        all_posts = []
        for user, posts in self.posts.items():
            if user in user_ids:
                all_posts.extend(posts)
        if not len(all_posts):
            return []
        top_k = 10 if len(all_posts)>=10 else len(all_posts)
        top_k_posts = sorted(all_posts, key = lambda post: post["timer"], reverse = True)
        return [top_k_posts["tweet_id"] for top_k_posts in top_k_posts[:top_k]]


    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follower_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follower_map[follower_id]:
            self.follower_map[follower_id].remove(followee_id)
        