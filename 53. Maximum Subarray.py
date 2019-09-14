class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(N) Solution
        ans = min(nums)
        sum = 0
        for i in range(len(nums)):
            if sum < 0:
                sum = nums[i]
            else:
                sum += nums[i]
            
            if ans < sum:
                ans = sum
        
        return ans

        # Time Limit Exceeded - O(n^2)
        # len_nums = len(nums)
        # ans = nums[0]
        # for i in range(len_nums):
        #     for j in range(i, len_nums):
        #         if ans < sum(nums[i: j]):
        #             ans = sum(nums[i: j])
        # return ans