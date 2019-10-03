class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if set(nums[i:]) == {0}:
                break
            elif nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1