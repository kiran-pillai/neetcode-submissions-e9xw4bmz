class Solution:
    """
    Naive: reverse the string and see if it is equal to each other
    """
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([char.lower() for char in s if char.isalnum()])
        l, r = 0, len(cleaned_s)-1
        while l<r:
            if cleaned_s[l]!=cleaned_s[r]:
                return False
            l+=1
            r-=1
        return True

        

