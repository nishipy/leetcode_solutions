class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i  = 0
        total = 0
        while i < len(s) - 1:
            if romanmap[s[i]] < romanmap[s[i+1]]:
                total += (romanmap[s[i+1]] - romanmap[s[i]])
                i += 2
            else:
                total += romanmap[s[i]]
                i += 1
                print(total)
        if i == len(s) - 1:
            total += romanmap[s[-1]]
        
        return total