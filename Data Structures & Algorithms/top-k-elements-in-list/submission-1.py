class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapped={}
        for num in nums:
            if num in mapped:
                mapped[num]+=1
            else:
                mapped[num]=1
        
        ordered_map=sorted(mapped.items(),reverse=True,key=lambda item:item[1])
        final_items=ordered_map[0:k]
        return list(map(lambda x: x[0], final_items))
               
        