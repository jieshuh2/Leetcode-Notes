#Combination
#Distinct input array. Repetive Infinite Candidates.
#Combanation Trick: 
#       Use idx as a parameter
#       Only use the candidate after the idx to avoid repetition
# Backtracking: 
#       Remember to set value and path back before going to another branch
#       Remember to use copy before append

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def dfs(idx, currentsum):
            if currentsum == 0:
                res.append(current.copy())
                return
            if idx >= len(candidates):
                return
            currentsum -= candidates[idx]
            if currentsum >= 0:
                current.append(candidates[idx])
                dfs(idx, currentsum)
                current.pop()
            currentsum += candidates[idx]
            dfs(idx + 1, currentsum)
        dfs(0, target)
        return res