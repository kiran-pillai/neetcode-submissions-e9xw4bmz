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
        seen = set()
        max_substr= 0
        l, r = 0, 0 
        while r<len(s):
            if s[r] not in seen:
                max_substr = max(max_substr, r-l+1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            r+=1
        return max_substr

                