import math
class Solution:
    """
    Naive solution
    """
    # def maxArea(self, heights: List[int]) -> int:
    #     def get_area(l,r,l_val,r_val):
    #         width=r-l
    #         height=min(l_val,r_val)
    #         return width*height 
    #     max_area=0
    #     final_container=[]
    #     for i in range(len(heights)):
    #         for j in range(i+1,len(heights)):
    #             area=get_area(i,j,heights[i],heights[j])
    #             if area>max_area:
    #                 max_area,final_container=area,[heights[i],heights[j]]
    #     return max_area
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        def get_area(l,r,l_val,r_val):
            width=r-l
            height=min(l_val,r_val)
            next_dir='r' if r_val<=l_val else 'l'
            return width*height,next_dir
        l=0
        r=len(heights)-1
        while l<r:
            area, next_dir=get_area(l,r,heights[l],heights[r])
            max_area=max(max_area,area)
            if next_dir=='l':
                l+=1
            else:
                r-=1 
        return max_area



