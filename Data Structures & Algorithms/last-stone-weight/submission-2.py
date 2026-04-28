import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)
        while len(max_heap)>1:
            max1, max2 = heapq.heappop_max(max_heap), heapq.heappop_max(max_heap)
            if max1>max2:
                heapq.heappush_max(max_heap,max1-max2)
        
        return max_heap[0] if len(max_heap) else 0

            