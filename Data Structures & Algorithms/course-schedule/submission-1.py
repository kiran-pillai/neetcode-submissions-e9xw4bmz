from collections import defaultdict
"""
dfs on adjacency list 
    - If there is a cycle return False
    - If pre-req can be completed that return True
"""
class Solution:
    def hasCycle(self, course, seen, mapping):
        if course in seen:
            return True
        seen.add(course)
        for pre in mapping[course]:
            if self.hasCycle(pre, seen, mapping):
                return True
        seen.remove(course)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        seen = set()
        for course, pre in prerequisites:
            mapping[course].append(pre)
        for course in range(numCourses):
            hasCycle = self.hasCycle(course, seen, mapping)
            print(hasCycle)
            if hasCycle:
                return False
        return True


