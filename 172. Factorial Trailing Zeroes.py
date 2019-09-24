class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        i = 1
        while 5**i <= n:
            ans += n//(5**i)
            i+=1
        return ans