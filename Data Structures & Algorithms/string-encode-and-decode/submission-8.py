class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for s in strs:
            string+=f"{len(s)}#{s}"
        return string
        """
        3#fds
        2:5
        """
    def decode(self, s: str) -> List[str]:
        l,r = 0, 0
        final_arr = []
        print(s)
        while r<len(s):
            if s[r] == "#":
                length = int(s[l:r])
                word = s[r+1:r+length+1]
                final_arr.append(word)
                r+=length+1
                l = r
            else:
                r+=1
        return final_arr
    
            
            
            
            


