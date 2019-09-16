class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for _ in range(numRows):
            if not ans:
                nextRow = self.createRow([])
            else:
                nextRow = self.createRow(ans[-1])
            ans.append(nextRow)
        return ans
            
    def createRow(self, prevRow):
        len_prevRow = len(prevRow)
        if len_prevRow <= 1:
            return [1]*(len_prevRow+1)
        else:
            l = [1]
            l.extend([sum(prevRow[i:i+2]) for i in range(len_prevRow-1)])
            l.append(1)
            return l