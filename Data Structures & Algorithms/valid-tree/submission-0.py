from collections import defaultdict
class Solution:
    def is_tree(self, node, parent, seen, adjList):
        if node in seen:
            return False
        seen.add(node)
        print(node)
        for neighbor in adjList[node]:
            if neighbor == parent:
                continue
            if not self.is_tree(neighbor, node, seen, adjList):
                return False
        return True
        

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)
        seen = set()
        if not self.is_tree(0,-1, seen,adjList):
            return False
        return len(seen) == n

        