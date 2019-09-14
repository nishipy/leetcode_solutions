class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                if hashtable[target-nums[i]] != i:
                    return [i, hashtable[target-nums[i]]]



#class Solution(object):
#    def twoSum(self, nums, target):
#        l = len(nums)
#        for i in range(l-1):
#            for j in range(l)[i:]:
#                if nums[i] + nums[j] == target:
#                    return [i, j]