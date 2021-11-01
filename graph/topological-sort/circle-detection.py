#Circle detection in dependency graph. Use visited set. add and pop trick
#Once we detect a valid vertex we put that into detect list so the next time we see it we know it is valid
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep = {k:[] for k, i in prerequisites}
        visited = set()
        detect = set()
        for k, i in prerequisites:
            dep[k].append(i)
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
            detect.add(v)
            return True
        for i in range(numCourses):
            res = dfs(i)
            if not res:
                return False
        return True