class Solution:
    def isValid(self, s: str) -> bool:
        mapped={'(':')', '{': '}', '[':']'}
        expected=[]
        for char in s:
            if char in mapped:
                expected.append(mapped[char])
            elif char not in mapped:
                if len(expected)==0:
                    return False
                if char!=expected.pop():
                    return False
        if len(expected)>0:
            return False
        return True