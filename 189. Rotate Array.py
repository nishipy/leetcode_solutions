class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            tmp_ = nums.pop()
            nums.insert(0, tmp_)



        # nums = nums[-k].extend(nums[:-k])