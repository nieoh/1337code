class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ret = ''
        if not str:
            return 0
        if ord(str[0]) == 32:
            i = 0
            while i < len(str) and ord(str[i]) == 32:
                i += 1
            str = str[i:]
        if not str:
            return 0    
        if ord(str[0]) == 45:
            ret += '-'
            str = str[1:]
        
        elif ord(str[0]) == 43:
            str = str[1:]
            
        def helper(str, ret):
            if not str:
                return ret
                
            if ord(str[0]) >= 48 and ord(str[0]) <= 57:
                
                ret += str[0]
                return helper(str[1:], ret)
            else:
                return ret
        
        ret = helper(str, ret)
        if not ret or ret == '-':
            return 0
        
        if ret[0] == '0':
            i = 0
            while i < len(ret) and ret[i] == '0':
                i += 1
            ret = ret[i:]
            
        elif ret[0] == '-':
            i = 1
            while i < len(ret) and ret[i] == '0':
                i += 1
            ret = '-' + ret[i:]
        sign = ''
        
        if not ret:
            return 0
        
        if ret[0] == '-':
            sign = '-'
            ret = ret[1:]
        if len(ret) > len("2147483648"):
            if sign == '-':
                return -2147483648
            else:
                return 2147483647
        if len(ret) == 10:
            if sign == '-' and ret > "2147483648":
                return -2147483648
            elif sign == '' and ret > "2147483647":
                return 2147483647
        if not ret:
            return 0
        return int(sign+ret)
