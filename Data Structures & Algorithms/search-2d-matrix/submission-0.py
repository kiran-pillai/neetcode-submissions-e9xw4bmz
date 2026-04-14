class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            length=len(m)
            l=0
            r=length-1
            while l<=r:
                middle_index = (l + r) // 2
                middle_value = m[middle_index]
                if middle_value==target:
                    return True
                elif target > middle_value:
                    l = middle_index + 1
                elif target < middle_value:
                    r = middle_index -1 
        return False