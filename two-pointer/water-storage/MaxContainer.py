# Water storage problem we only care about the minimum of two pointer.
# If either bound is lower, we should move this bound. (Moving a higher bound will not give us useful)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxWater = 0
        while (l < r):
            maxWater = max(maxWater, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater