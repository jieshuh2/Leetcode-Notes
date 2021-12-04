# Need notice:
# 1. Search the shorter array.  For two reason : 
#   1) Never out of bound. The total number of the left is alwasy less than half. 
#   2) time complexity.
# 2. Half length: (total + 1) // 2 (even on the first idx). idx1 + idx2 = halflength - 2
# 3. Since we are partition the array, it is legal for partition point to be out of bound.
#   1) The starting left idx will be -1 instead of 0
#   2) Set the left bound to be -inf and right to be inf

class Solution:
    def midpoint(self, arr): #caculate the median of an array
        halfidx = (len(arr) - 1)//2
        if len(arr) % 2 == 0:
            return (arr[halfidx] + arr[halfidx + 1]) / 2
        else:
            return arr[halfidx]
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        l = -1
        r = len(nums1)
        while l < r:
            idx1 = l + (r - l) // 2
            idx2  = half - idx1 - 2
            num1Left = nums1[idx1] if idx1 >= 0 else -math.inf
            num1Right = nums1[idx1 + 1] if idx1 + 1 < len(nums1) else math.inf
            num2Left = nums2[idx2] if idx2 >= 0 else -math.inf
            num2Right = nums2[idx2 + 1] if idx2 + 1 < len(nums2) else math.inf
            if  num1Left <= num2Right and num2Left <= num1Right:
                l = idx1
                break
            elif num1Left > num2Right:
                r = idx1
            else:
                l = idx1 + 1
        idx1 = l
        idx2  = half - idx1 - 2
        num1Left = nums1[idx1] if idx1 >= 0 else -math.inf
        num1Right = nums1[idx1 + 1] if idx1 + 1 < len(nums1) else math.inf
        num2Left = nums2[idx2] if idx2 >= 0 else -math.inf
        num2Right = nums2[idx2 + 1] if idx2 + 1 < len(nums2) else math.inf
        if total % 2 == 0:
            return (max(num1Left, num2Left) + min(num1Right, num2Right)) / 2
        else:
            return max(num1Left, num2Left)
        