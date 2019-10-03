class Solution:
    def missingNumber(self, nums: list) -> int:
        maxn = max(nums)
        minn = min(nums)
        diff = sum(range(minn, maxn+1)) - sum(nums)
        if minn > 0:
            return 0
        elif diff == 0:
            return maxn + 1
        else:
            return diff