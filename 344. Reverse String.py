class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        bound = int(len(s)/2)
        for i in range(bound):
            tmp_left = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = tmp_left