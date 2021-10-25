#New string that is different from all string given
#We want our new string to be different from all strings given
# We make our new string to be different to the ith string at ith number.
#Therefore, for all strings given, our new string is at least one char different.
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        n = len(nums[0])
        idx = 0
        while idx < len(nums):
            c = int(nums[idx][idx])
            cc = 1-c         #the complement of the ith num at position i
            res += str(cc)
            idx += 1
        while idx < n:
            res += "0"
        return res
            