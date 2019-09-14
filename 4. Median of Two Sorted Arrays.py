class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j = 0, 0
        length = 0
        
        if len(nums1) + len(nums2) % 2 == 0:
            half = (len(nums1) + len(nums2)) / 2
        else:
            half = ((len(nums1) + len(nums2)) / 2) + 1
            for t in range(half):
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    j += 1
            return max(nums1[i], nums2[j])
    