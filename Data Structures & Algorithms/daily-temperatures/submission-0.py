class Solution:
    """
    Naive loop through each temp and see where temp exceeds
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i, temp in enumerate(temperatures):
            if i==len(temperatures)-1:
                res.append(0)
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temp:
                    res.append(j-i)
                    break
                elif j==len(temperatures)-1:
                    res.append(0)
        return res
        