from collections import defaultdict
"""
dfs on adjacency list 
    - If there is a cycle return False
    - If pre-req can be completed that return True
"""
class Solution:
    def dfs(self, node, seen, al):
        if node in seen:
            return False
        seen.add(node)
        for neighbor in al[node]:
            if not self.dfs(neighbor, seen, al):
                return False
        seen.remove(node)
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al = defaultdict(list)
        for pair in prerequisites:
            course, pre = pair
            al[course].append(pre)
        print(al)
        seen = set()
        for course in range(numCourses):
            canCompleteCourse = self.dfs(course,seen, al)
            print("canCompleteCourse",canCompleteCourse)
            if not canCompleteCourse:
                return False
        return True
