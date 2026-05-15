import heapq
class Solution:
    """
    Brute force:
        - loop through slot 1
        - compare each availability to slot 2 and see if there is overlap
        - if there is overlap append both time slots to res


        [10, 20] [3, 30]
    """
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        res = []
        for slot1B, slot1E in slots1:
            if slot1E - slot1B < duration:
                continue
            for slot2B, slot2E in slots2:
                if slot2E - slot2B < duration:
                    continue
                if slot2B + duration <= slot1E:
                    print(slot2E, slot1E)
                    start = max(slot1B, slot2B)
                    end =  min(slot1E, slot2E)
                    if end - start >=duration:
                        heapq.heappush(res, [start, start + duration ])
        return res[0] if len(res) else res
