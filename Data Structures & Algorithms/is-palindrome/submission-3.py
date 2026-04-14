class Solution:
    """
    Naive: reverse the string and see if it is equal to each other
    """
    def isPalindrome(self, s: str) -> bool:
        def clean_str(st:str) -> str:
            return st.replace(" ", "").lower().replace(".", "").replace("!","").replace("?","").replace("'","").replace(",","").replace(":","")
        reversed_s="".join(reversed(clean_str(s)))
        print(reversed_s)
        print(clean_str(s))
        return reversed_s==clean_str(s)
        