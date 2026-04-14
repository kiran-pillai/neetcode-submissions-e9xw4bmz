class Solution:
    """
    min(heights) * indexEnd-indexStart
    Naive
    """
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     max_area=max(heights)
    #     stack=[]
    #     if len(heights)==1:
    #         return heights[0]
    #     for i in range(len(heights)):
    #         for j in range(i+1,len(heights)):
    #             area=(j-i+1) * min(heights[i:j+1])
    #             print(heights[i:j+1], area, j-i)
    #             stack.append(area)
    #     return max(max(stack),max_area)
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]

        for i, height in enumerate(heights):
            start=i
            while stack and height<stack[-1][0]:
                poppedHeight, poppedIndex=stack.pop()
                area=(i-poppedIndex) * poppedHeight
                maxArea=max(area,maxArea)
                start=poppedIndex
            stack.append([height, start])
        
        for i, box in enumerate(stack):
            height, index = box
            area=(len(heights)-index)*height
            maxArea=max(maxArea,area)
        return maxArea
