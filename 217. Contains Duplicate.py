class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == len(list(set(nums))):
            return False
        else:
            return True