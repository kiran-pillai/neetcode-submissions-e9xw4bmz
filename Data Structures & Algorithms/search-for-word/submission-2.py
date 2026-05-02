from collections import Counter
"""
Base cases:
    Failures
    - Exceed row or column count
    - Exceed length of word
        return 
    - Got to lower right tile 
        return False
    
    Success
    - "".join(sol) == word
        return True
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = set()
        def dfs(r,c,i):
            if min(r,c)<0 or r>=ROW or c>=COL or (r,c) in seen or word[i]!=board[r][c]:
                return False
            if i == len(word) - 1:
                return True
            seen.add((r,c))
            res = (dfs(r+1,c,i+1) or 
                  dfs(r-1,c,i+1) or 
                  dfs(r,c+1,i+1) or 
                  dfs(r,c-1,i+1))
            seen.remove((r,c))
            return res

        for r in range(ROW):
            for c in range(COL):
                if dfs(r,c,0):
                    return True
        return False