class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }

        if any([s.startswith(v) for v in pairs.values()]):
            return False
        
        n_lefts = sum([s.count(v) for v in pairs.values()])
        n_rights = sum([s.count(k) for k in pairs.keys()])
        if n_lefts != n_rights:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            else:
                if s[i] != pairs[stack.pop(-1)]:
                    return False
        
        return True            
