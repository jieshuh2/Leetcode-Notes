#Quick Select:
# [3,   2,  1,  4,  6,  5]
#       p   i           ^
#      pidx scan       piviot
# Loop through the array. The number at the left of pidx is always smaller than pivot.
# If i scanned is larger than pointed value, swap it with pidx and move the pointer
# Finally, swap piviot with pidx. So all the number to the left is smaller and all the number to the right is larger

# Avg time complexity is O(n) : n + n/2 + n/4 + ... = O(n) Worst: O(n**2)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r, k):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i] #swap
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if k == p:
                return pivot
            elif k < p:
                return quickSelect(l, p - 1, k)
            else: #k > p
                return quickSelect(p + 1, r, k)
            # [3,2,1,4,6,5]
        return quickSelect(0, len(nums) - 1, k)
# Another solution: heapify: O(n), heappop: k*O(log(n))
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        heapify(nums)
        for i in range(k + 1):
            res = heappop(nums)
        return res