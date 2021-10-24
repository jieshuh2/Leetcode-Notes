#Combination
#Repetitive input array. Repetitive fixed-Size Candidate.
#Trick: 
#       Use dictionary Use key as idx array
#       Transform to combsum
# Backtracking: 
#       Remember to set all values and path back before going to another branch
#       Remember to use copy before append

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dic = {}
        for i in candidates:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        keys = list(dic.keys())
        res = []
        current = []
        def dfs(idx, target):
            if target < 0:
                return
            if target == 0:
                res.append(current.copy())
                return
            if idx >= len(keys):
                return 
            key = keys[idx]
            if dic[key] > 0:
                dic[key] -= 1
                target -= key
                current.append(key)
                dfs(idx, target)
                current.pop()
                dic[key] += 1
                target += key
            dfs(idx + 1, target)
        dfs(0, target)
        return res
        

