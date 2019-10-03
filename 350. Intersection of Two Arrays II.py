class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        len_1 = len(nums1)
        len_2 = len(nums2)
        nums1.sort()
        nums2.sort()
        ans = []
        i = 0
        j = 0
        while i<len_1 and j<len_2:
            if nums2[j] == nums1[i]:
                ans.append(nums2[j])
                i += 1
                j += 1
            elif nums2[j] > nums1[i]:
                i += 1
            else:
                j += 1
        return ans