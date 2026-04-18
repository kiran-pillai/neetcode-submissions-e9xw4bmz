from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Use a dictionary track freq of elems
        Sort values by Descending
        slice at k 
        """
        freq_map = Counter(nums)
        sorted_freq_map = sorted(freq_map.items(), key = lambda item: item[1], reverse = True)
        return [item[0] for item in sorted_freq_map[:k]]
        