class Solution:
    def countSubstrings(self, s: str) -> int:
        if(len(s) == 1):
            return 1
        counter = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                isPalindrome = True
                while l<r:
                    if s[l] != s[r]:
                        isPalindrome = False
                        break
                    l+=1
                    r-=1
                if isPalindrome:
                    counter +=1
        return counter