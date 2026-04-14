class Solution:
    """
    Naive:
    Iterate through each item individually and compare if it's the same as neighbor
    Keep track of visited elements to skip with hashmap

    Time complexity: o(n*n*nlogn) -> o(n^3logn)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited={}
        final_answer=[]
        sorted_strs={}
        for s in strs:
            sorted_strs[s]=sorted(s)
        for i in range(len(strs)):
            output=[strs[i]]
            if strs[i] not in visited:
                for j in range(i+1,len(strs)):
                    if sorted_strs[strs[i]]==sorted_strs[strs[j]]:
                        output.append(strs[j])
                        visited[strs[j]]=True
                final_answer.append(output)
                visited[strs[i]]=True
        return final_answer

    
        
