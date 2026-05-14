from collections import Counter
"""
Create counter of s
while k in list(freqMap.values())
- iterate through
- delete key
- build string


SLIDING WINDOW
Create counter of s

- If there K is in the values of counter, keep iterating
- Iterate over string
    - calculate once you've seen a new non-repeating value
        - use set and reset or check one before current iteratee
        - check r-l if == k  -> update updated_str and freqMap, move l = r reset seen

STACK 
- keep counter
- keep stack
- while k in counter.values()
- iterate through stack
    - if prev value == current value
    - increase count
    - else: count =0
- return .join of stack



"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1]+=1
            else:
                stack.append([char, 1])
            if stack[-1][1] == k:
                stack.pop()
        return "".join([char[0]*char[1] for char in stack])
                
            
