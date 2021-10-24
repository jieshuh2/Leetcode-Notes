#Permutaion: 
#   Fixed output length
#   Distinct input array. Non repetitive output
#Permutation trick:
#   Pop each member in array and add them back to the result.
#   Base case: length input is 0 and length output is the equal to the original array
#   This solution is not as flexible as permute2. Reference permute 2

class Solution(object):
    def permute(self, nums):
        """
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result