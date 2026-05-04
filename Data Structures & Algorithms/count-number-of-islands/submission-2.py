from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        seen = set()
        islands = 0
        ROW, COL = len(grid), len(grid[0])
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            seen.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for ar, ac in directions:
                    nr, nc = r + ar, c + ac
                    if nr not in range(ROW) or nc not in range(COL) or grid[nr][nc]=="0" or (nr,nc) in seen:
                        continue
                    q.append((nr, nc))
                    seen.add((nr,nc))
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in seen:
                    bfs(r,c)
                    islands+=1
        return islands