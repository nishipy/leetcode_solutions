class Solution:
    def isHappy(self, n: int) -> bool:
        hashTable = {}
        while n != 1:
            n = self.sumSquareDigits(n)
            if n in hashTable:
                return False
            else:
                hashTable[n] = 1
        return True

    def sumSquareDigits(self, m:int) -> int:
        s = 0
        for i in str(m):
            s += int(i)**2
        return s