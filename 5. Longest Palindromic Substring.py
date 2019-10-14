class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s < 2:
            return s
        else:
            rs = s[0]
            for i in range(len_s):
                if len(rs) > len(s[i:]):
                    return rs
                for j in reversed(range(i+1, len_s)):
                    if self._is_palindromic(s[i:j+1]) and len(rs) < len(s[i:j+1]):
                        rs = s[i:j+1]
                        break
            return rs

    def _is_palindromic(self, s: str) -> bool:
        l = len(s)
        if l%2==0:
            return s[:l/2] == s[l/2:]
        else:
            return s[:l/2] == s[l/2+1:]


