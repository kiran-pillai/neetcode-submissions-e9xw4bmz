import copy
from collections import Counter
class Solution:
    """
    Q: When do we increment l?
    A: When s not in countS1, l+=1

    Q: How do we keep track of how much of the substr we have completed?
    A: First thought is duplicate countS1, decrement everytime we encounter char
       -if all vals are 0 return True
       -if char not in count reset duplicate to equal countS1

    Q: Can we make the logic for keeping track simpler?
    A: Prbly, how can we track  

    Q: How do we make this a sliding window technique, where is l coming into play?
    A: 
    """
    #Hash map
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     countS1={}
    #     for s in s1:
    #         countS1[s]=countS1.get(s,0) + 1
    #     for i in range(len(s2)):
    #         countS2, curr = {}, 0
    #         for j in range(i, len(s2)):
    #             countS2[s2[j]]=countS2.get(s2[j], 0) + 1
    #             if countS2[s2[j]] > countS1.get(s2[j], 0):
    #                 break
    #             if countS2[s2[j]] == countS1.get(s2[j], 0):
    #                 curr+=1
    #             if curr==len(countS1):
    #                 return True
    #     return False
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s2), len(s1)
        count1 = Counter(s1)
        for i in range(m-n+1):
            substr=s2[i:i+n]
            count2=Counter(substr)
            if count1==count2:
                return True
        return False


            