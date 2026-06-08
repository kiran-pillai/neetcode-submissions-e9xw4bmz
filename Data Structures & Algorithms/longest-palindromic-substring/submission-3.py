class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        # Odd case
        for i in range(len(s)):
            l, r  = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if len(longest)<(r-l)+1:
                    longest = s[l:r+1]
                l-=1
                r+=1
        # Even case
        for i in range(len(s)):
            l, r  = i, i + 1
            while r<len(s) and s[l] == s[r] and l>=0:
                if len(longest)<(r-l)+1:
                    longest = s[l:r+1]
                l-=1
                r+=1
        return longest

