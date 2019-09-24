class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

        # hashTable = {}
        # bound = len(nums) / 2
        # for i in nums:
        #     if i in hashTable:
        #         hashTable[i] += 1
        #     else:
        #         hashTable[i] = 1
            
        # for k, v in hashTable.items():
        #     if v > bound:
        #         return k