class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        shortest_str = min(strs, key=len)
        #len_map = {}
        #for i in range(len(strs)):
        #    len_map[len(strs[i])] = i
        #for j in range(min(len_map.keys())+1)[::-1]:
        
        for i in range(len(shortest_str))[::-1]:
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                return shortest_str[:i+1]
        
        return ''