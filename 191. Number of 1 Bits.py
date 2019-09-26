class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = format(n, '032b')
        ans = 0
        for i in s:
            if i == '1':
                ans += 1
        return ans