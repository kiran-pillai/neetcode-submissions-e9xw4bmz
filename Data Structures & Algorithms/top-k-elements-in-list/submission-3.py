from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        sortedMap = sorted(freqMap.items(), key = lambda item: item[1], reverse = True)
        return [item[0]for item in sortedMap[:k]]
            