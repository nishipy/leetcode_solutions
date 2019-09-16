class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = n // 2
        ans = 1
        for i in range(1, q+1):
            ans += self.comb(n - i, i)
        return ans

    def comb(self, n, m):
        denom, numer = 1, 1
        if m != 0:
            for i in range(m):
                denom *= m - i
                numer *= n - i
        return numer / denom