from collections import defaultdict
class Solution:
    def dfs(self, edge, seen, adjList):
        if edge in seen:
            return
        seen.add(edge)
        for edge in adjList[edge]:
            self.dfs(edge,seen,adjList)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        seen = set()
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        count = 0
        for edge in range(n):
            if edge not in seen:
                self.dfs(edge,seen,adjList)
                count+=1
        return count
            