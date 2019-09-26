class Solution:
    def rob(self, nums):
        last, now = 0, 0
        for n in nums:
            last, now = now, max(last + n, now)
        return now
