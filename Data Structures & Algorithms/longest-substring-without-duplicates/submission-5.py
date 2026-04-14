class Solution:
    """
    initialize l, r = 0
    iterate through each char
    use hashset
    When do we increment r?
    - if current char is not in hash set

    when do we increment l?
    - if current char is in hashset
    - erase hashset

    How can we account for the first elem?

    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l, r = 0, 1
        seen=set()
        max_substr=1
        print(s)
        seen.add(s[l])
        if len(s) ==0:
            return 0
        while r!=len(s):
            if s[r] in seen:
                max_substr=max(max_substr,len(seen))
                seen.remove(s[l])
                l+=1
            else:
                seen.add(s[r])
                print(seen)
                max_substr=max(max_substr,len(seen))
                r+=1
        return max_substr
            
        
