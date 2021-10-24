#Permutaion: 
#   Fixed output length
#   Repetitive input array. Non-repetitive output
#Permutation trick:
#   Use dictionary to avoid repetition at given idx
#   Pop each member in array and add them back to the result.
#   Base case: length input is 0 and length output is the equal to the original array

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 0
            dic[n] += 1
        res = []
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in dic:
                if dic[n] > 0:
                    dic[n] -= 1
                    perm.append(n)
                    dfs(perm)
                    dic[n] += 1
                    perm.pop()
        dfs([])
        return res
                