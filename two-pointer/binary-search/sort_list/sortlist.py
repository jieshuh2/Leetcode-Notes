# SortedList is base on the binary search
#   bisect_left:  The first position to insert
#   bisect_right: The end position to insert
#   refers to start and end in the same folder.
# For this problem, we search for a range from n - t to n + t in our array.
# If no number within this range exist, then the left position of this range should be the same as the right. 
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        sortList = SortedList()
        for i, n in enumerate(nums):
            if i > k:
                sortList.remove(nums[i - k - 1])
            Psmall = bisect_left(sortList, n - t) 
            Plarge = bisect_right(sortList, n + t)
            if Psmall != Plarge:
                return True
            sortList.add(n)
        return False