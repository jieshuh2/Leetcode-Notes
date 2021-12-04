# A two pointer O(n) solution with O(1) memory. 
# 1) We only care of the minimum bound so we only care of the minimum pointer. 
# 2) We always have enough information about the position that is near to our pointer.
# 3) The amount of water in each position: min(maxheightleft, maxheightright) - height
#       For simplicity, the leftbound and rightbound include the point itself. 
class Solution:
    def trap(self, height: List[int]) -> int:
        size = 0
        l = 0
        r = len(height) - 1
        leftbound = height[l]
        rightbound = height[r]
        while (l <= r):
            if leftbound <= rightbound:
                leftbound = max(leftbound, height[l])
                size += leftbound - height[l]
                l += 1
            else:
                rightbound = max(rightbound, height[r])
                size += rightbound - height[r]
                r -= 1
        return size

