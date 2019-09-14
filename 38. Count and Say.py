class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        if n == 1:
            return ans
        else:
            for _ in range(n-1):
                ans = self.helper(str(ans))
            return ans

    def helper(self, s):
        i = 0
        rs = ''
        while i < len(s):
            length = 1
            for s_ in s[i+1:]:
                if s[i] == s_:
                    length += 1
                else:
                    break
            rs += str(length) + str(s[i])
            i += length
            
        return rs