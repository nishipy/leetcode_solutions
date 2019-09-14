class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)

        
        # return list(set(nums))
        
        # len_nums = len(nums)
        # if len_nums > 1:
        #     i = 0
        #     while i < len_nums - 1:
        #         length = 0
        #         for n in nums[i:]:
        #             if n == nums[i]:
        #                 length += 1
        #             else:
        #                 break
        #         if length > 1:
        #             del nums[i+1:i+length]
        #         i += 1
        #         len_nums = len(nums)

