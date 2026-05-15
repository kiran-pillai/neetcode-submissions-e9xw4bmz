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
        minn = [float('inf')]
        for slot1B, slot1E in slots1:
            if slot1E - slot1B < duration:
                continue
            for slot2B, slot2E in slots2:
                if slot2E - slot2B < duration:
                    continue
                start = max(slot1B, slot2B)
                end =  min(slot1E, slot2E)
                if end - start >=duration and start<minn[0]:
                    minn = [start, start + duration]
        return [] if minn[0] == float('inf') else minn
