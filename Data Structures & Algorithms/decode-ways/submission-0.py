class Solution:
    """
    112345
    123
    """
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [1,1]
        for i, char in enumerate(s[1:],1):
            # Make sure num isn't 0
            count = 0
            if char!= "0":
                count+=dp[i]
            if 10<=int(s[i-1:i+1])<=26:
                count+=dp[i-1]
            dp.append(count)
            # Make sure double num is between 10 and 26
        return dp[-1]


            

            
