from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        seen = set()
        islands = 0
        ROW, COL = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            seen.add((r,c))
            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for ar, ac in directions:
                    nr, nc =  r + ar, c + ac
                    if nr not in range(ROW) or nc not in range(COL) or (nr,nc) in seen or grid[nr][nc] =="0":
                        continue
                    q.append((nr,nc))
                    seen.add((nr,nc))
                     

        for r in range(ROW):
            for c in range(COL):
                cell = grid[r][c]
                if (r,c) not in seen and cell == "1":
                    bfs(r,c)
                    islands+=1
        return islands