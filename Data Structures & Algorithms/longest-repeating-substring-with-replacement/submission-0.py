class Solution:
    """
    Q: How do we keep track of longest substr?
    A: Do og sliding window and track start and end index

    Q: How do we keep track of longest substr and potential replacements to increase it?
    A: Track longest sub str and track end index. 

    Q: How can we use the end index to track when the next occurence occurs
    A: If we track the end index and repeating char, ex: {"k":2}, we can use that 
       to see if end_index + k == next occurence of k's index, if it does we increment the count

    Q: How can we keep track of two potential counts? One that ended and may grow and one that is
       happening currently?
    A: We should track char and counts in dictionary. Only increment dictionaries when repeated chars
       or chars last index + k <= next occurence

    Q: What happens if there are multiple occurences of the char? ex: "fffagffffff" k=1
    A: If char already exists then we keep a running counter and only update dictionary when 
       it running counter exceeds current value

    Q: How do we properly keep track of all k we are alloted? ex: "ffaffdfzzzzzz" k=2
    A: Track k in a seperate var, alloted_replacements, decrement as needed 
    
    Q: when do we increment l?
    A: When s[l] != s[r], we move l=r and r+=1

    Q: What's the proper way of tracking if alloted is out of bounds or not? 
    A: 


    Neetcode way:
    1). Store Frequence maps
    2). Intialize l, r =0, 0
    3). check each window at a time
        a). if a particular window is "valid", len - highest_count >=k, potentially update max
        b). Update l when window is no longer "valid"


    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res, l, r = 0, 0, 0
        while r< len(s):
            count[s[r]]=1 + count.get(s[r],0)
            if (r-l + 1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res= max(res, r-l+1)
            r+=1

        return res
        
                

        
