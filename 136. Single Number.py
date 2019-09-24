class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable:
                hashTable[nums[i]] += 1
            else:
                hashTable[nums[i]] = 1
        for k, v in hashTable.items():
            if v == 1:
                return k