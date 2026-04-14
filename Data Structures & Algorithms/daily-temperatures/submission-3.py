    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res=[0]*len(temperatures)
    #     stack=[]

    #     for i, t in enumerate(temperatures):
    #         while stack and t>stack[-1][0]:
    #             temp, tempIndex= stack.pop()
    #             res[tempIndex]=i-tempIndex
    #         stack.append([t,i])
    #     return res
class Solution:
    """
    Naive loop through each temp and see where temp exceeds
    """
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res=[]
    #     for i, temp in enumerate(temperatures):
    #         if i==len(temperatures)-1:
    #             res.append(0)
    #         for j in range(i+1,len(temperatures)):
    #             if temperatures[j]>temp:
    #                 res.append(j-i)
    #                 break
    #             elif j==len(temperatures)-1:
    #                 res.append(0)
    #     return res


    """
    Initialize a output array, length of temp array
    Initialize a stack
    Iterate through the array
    Create a nested while loop
        - When current item >= last item of stack
            - pop it and add to temp array at i-storedIndex
            -   
[[2,30]]
[1,2,3]
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                index, val = stack.pop()
                output[index] = i - index
            stack.append([i, temp])
        return output

    

        