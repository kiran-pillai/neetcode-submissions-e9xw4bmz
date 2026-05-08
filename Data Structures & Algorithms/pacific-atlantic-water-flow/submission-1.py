class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(grid), len(grid[0])
        pac = set()
        atl = set()

        def dfs(r, c, prevVal, visited):
            if r not in range(ROWS) or c not in range(COLS):
                return 
            if (r,c) in visited:
                return 
            if prevVal>grid[r][c]:
                return
            visited.add((r,c))
            dfs(r-1,c,grid[r][c],visited)
            dfs(r+1,c,grid[r][c],visited)
            dfs(r,c-1,grid[r][c],visited)
            dfs(r,c+1,grid[r][c],visited)

        for c in range(COLS):
            dfs(0, c, float('-inf'), pac)
            dfs(ROWS-1, c, float('-inf'), atl)
        for r in range(ROWS):
            dfs(r, 0, float('-inf'), pac)
            dfs(r, COLS - 1, float('-inf'), atl)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res



