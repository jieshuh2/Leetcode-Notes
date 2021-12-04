# For in place solution. The trick here is to prevent the overwrite of info that will be used.
# If we merge these two arrays backward, the length of zeros will gurantee that the place that we write will always already be processed.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        while(idx1 >= 0 and idx2 >= 0):
            if nums1[idx1] > nums2[idx2]:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            idx -= 1
        while(idx2 >= 0):
            nums1[idx] = nums2[idx2]
            idx -= 1
            idx2 -= 1