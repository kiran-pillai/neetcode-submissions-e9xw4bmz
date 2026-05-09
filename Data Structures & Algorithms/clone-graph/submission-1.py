from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node, seen):
            if node in seen:
                return seen[node]
            newNode = Node(val = node.val)
            seen[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor,seen))
            return newNode
        if node is None:
            return None
        seen = {}
        return dfs(node, seen)

                    
                

        
        
        