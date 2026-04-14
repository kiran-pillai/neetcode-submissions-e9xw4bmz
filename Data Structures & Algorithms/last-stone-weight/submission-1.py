class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        current_stones = sorted(stones)
        while len(current_stones)>1:
            max_stone, second_max = current_stones.pop(), current_stones.pop()
            diff = max_stone - second_max
            if diff>0:
                current_stones.append(diff)
                current_stones.sort()
        
        return current_stones[0] if len(current_stones)>0 else 0