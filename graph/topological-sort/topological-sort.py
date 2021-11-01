#Exactly the same pattern as circle detection. 
#use the output list so that it can be used as a global variable. A clock cannot be used globally. 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dep = {k:[] for k, i in prerequisites}
        visited = set()
        detect = set()
        for k, i in prerequisites:
            dep[k].append(i)
        output = []
        def dfs(v):
            if v in visited:
                return False
            if v in detect:
                return True
            visited.add(v)
            if v in dep:
                for i in dep[v]:
                    if not dfs(i):
                        return False
            visited.remove(v)
            output.append(v)
            detect.add(v)
            return True
        for v in range(numCourses):
            res = dfs(v)
            if not res:
                return []
        return output