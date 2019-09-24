class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_ = [x for x in s if x.isalnum()]
        len_s_ = len(s_) 
        if len_s_ <= 1:
            return True
        else:
            return s_[:len_s_//2] == s_[::-1][:len_s_//2]
