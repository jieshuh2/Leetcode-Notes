#The maxarray that ends at a given position is MaxArrayEndAt(i) = nums[i] + max(0, MaxArrayEndAt(i - 1)])
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        maxsum = -math.inf
        for n in nums:
            if res < 0:
                res = 0
            res += n
            maxsum = max(res, maxsum)
        return maxsum