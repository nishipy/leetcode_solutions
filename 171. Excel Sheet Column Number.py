class Solution:
    def titleToNumber(self, s: str) -> int:
        s_ = s[::-1]
        alpha2num = lambda c: ord(c) - ord('A') + 1
        ans = 0
        for i in range(len(s)):
            ans += alpha2num(s_[i]) * (26**(i))
        
        return ans