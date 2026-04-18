class Solution:
    """
    Naive: reverse the string and see if it is equal to each other
    """
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==1:
            return True
        
        
        cleaned_str =""
        for char in s.lower(): 
            if char.isalnum():
                cleaned_str += char
        
        l,r = 0, len(cleaned_str)-1   
        print(cleaned_str) 
        while l<r:
            print(r)
            if cleaned_str[l]!=cleaned_str[r]:
                return False
            r-=1
            l+=1
        return True


        

