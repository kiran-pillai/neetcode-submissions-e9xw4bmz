class Solution:
    """
    Naive: reverse the string and see if it is equal to each other
    """
    # def isPalindrome(self, s: str) -> bool:
    #     def clean_str(st:str) -> str:
    #         return st.replace(" ", "").lower().replace(".", "").replace("!","").replace("?","").replace("'","").replace(",","").replace(":","")
    #     reversed_s="".join(reversed(clean_str(s)))
    #     return reversed_s==clean_str(s)
        
    def isPalindrome(self, s: str) -> bool:

        def clean(st:str) -> str:
            return "".join([s.lower() if s.isalnum() else "" for s in st])
        cleaned_s=clean(s)
        if len(cleaned_s)==0:
            return True
        j=len(cleaned_s) - 1 
        for i,char in enumerate(cleaned_s):
            if j<=i:
                return True
            if char!=cleaned_s[j]:
                print(char, cleaned_s[j])
                return False
            j-=1
            
