class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for st in strs:
            string+=f"{len(st)}#{st}"
        return string
    def decode(self, s: str) -> List[str]:
        i=0
        final_arr=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            final_arr.append(s[j+1:j+1+length])
            i=j+length+1
        return final_arr
            
            
            
            


