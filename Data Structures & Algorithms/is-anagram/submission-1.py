from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreqMap= Counter(s)
        for char in t:
            if char not in sFreqMap:
                return False
            else:
                sFreqMap[char]-=1
                if sFreqMap[char] == 0:
                    del sFreqMap[char]
        return len(sFreqMap) == 0

            
            