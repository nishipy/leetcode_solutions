class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_needle == 0:
            return 0
        if len_haystack < len_needle:
            return -1
        
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:].startswith(needle):
                return i

        return -1
        