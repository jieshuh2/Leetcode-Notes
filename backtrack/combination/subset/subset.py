#Basic Combination without restriction
#Distinct input array
#For given element either choose or not choose. Proceeds to the next element
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        sub = []
        def dfs(i):
            if i == len(nums):
                sets.append(sub.copy())
                return
            dfs(i+1)
            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
        dfs(0)
        return sets