class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashTable = {}
        for i in range(len(s)):
            if s[i] in hashTable:
                hashTable[s[i]] += 1
            else:
                hashTable[s[i]] = 1
        for k, v in hashTable.items():
            if v == 1:
                return s.index(k)
        return -1