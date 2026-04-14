class Solution:
    """
    min(heights) * indexEnd-indexStart
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=max(heights)
        stack=[]
        if len(heights)==1:
            return heights[0]
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area=(j-i+1) * min(heights[i:j+1])
                print(heights[i:j+1], area, j-i)
                stack.append(area)
        return max(max(stack),max_area)
