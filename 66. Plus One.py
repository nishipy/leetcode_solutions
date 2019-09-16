class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus_one = int(''.join(map(str, digits))) + 1
        ans = [int(x) for x in str(plus_one)]
        return ans

        #return int(''.join(map(str, digits)))