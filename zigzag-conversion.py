#leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ret = ''
        if not s:
            return ret
        if numRows == 1:
            return s
        k = 2*numRows - 2
        
        
        ret += str(s[0::k])
        
        for i in range(1, numRows-1):
            for j, char in enumerate(s):
                if i == (j%k) or i == (-j%k):
                    ret += char
        ret += str(s[numRows-1::k])
        
        return ret
