class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        char_dict = {}
        ans = 0
        for i, ch in enumerate(s):
            if ch in char_dict:
                left = max(left, char_dict[ch]+1)
            char_dict[ch] = i
            ans = max(ans, i - left + 1)
        return ans