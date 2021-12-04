#standard writing of binary search.
#without the equal: find the first index of the given target
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)
        def bs(l, r, target):
            while l < r:
                mid = l + (r - l)//2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        start = bs(l, r, target)
        end = bs(l, r, target + 1) - 1
        if start > end:
            return [-1, -1]
        return [start, end]
    