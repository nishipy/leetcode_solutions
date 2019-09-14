class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0
        
        if x > 0:
            ans = int(str(x)[::-1])
        elif x < 0:
            ans = -1 * int(str(-x)[::-1])
        
        if ans > -(2**31) and ans < 2**31 - 1:
            return ans
        else:
            return 0