class Solution:
    """
    longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word == "".join(reversed(word)) and len(word)>len(longest):
                    longest = word
        return longest
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) ==1:
            return s
        longest = ""
        for i, char in enumerate(s):
            l, r = i, i
            while l>=0 and r<len(s):
                if s[l] != s[r]:
                    break
                if r-l+1>len(longest):
                    longest = s[l:r+1]
                r+=1
                l-=1
            l, r = i, i+1
            while l>=0 and r<len(s):
                if s[l] != s[r]:
                    break
                if r-l+1>len(longest):
                    longest = s[l:r+1]
                r+=1
                l-=1
        return longest
