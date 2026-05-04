from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        water = -1
        treasure = 0
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        seen = set()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == treasure:
                    q.append((r,c, 0))

        while q:
            r, c, count = q.popleft()
            seen.add((r,c))
            directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
            for ar, ac in directions:
                nr, nc = r + ar, c + ac
                if nr not in range(ROW) or nc not in range(COL) or grid[nr][nc] == -1 or (nr,nc) in seen:
                    print("first if",nr, nc)
                    continue
                if grid[nr][nc] == land:
                    print("second if", nr, nc)
                    grid[nr][nc] = count + 1
                q.append((nr,nc,count+1))


                    
        
