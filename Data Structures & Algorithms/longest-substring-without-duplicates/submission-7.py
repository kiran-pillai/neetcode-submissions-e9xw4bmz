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
        max_count = 0
        seen = set()
        l = 0
        for r, char in enumerate(s):
            if char in seen:
                while char in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(char)
            print(seen)
            max_count = max(max_count, r-l+1)
        return max_count
            
        
