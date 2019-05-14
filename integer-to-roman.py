class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        power = 0
        dict = {'0': ['VI', 'XI', 'I', 'V'], '1': ['LX', 'CX', 'X', 'L'], '2': ['DC', 'MC', 'C', 'D'], '3':['', '', 'M', '']}
        while num > 0:
            digit = num//(10**power) % 10
            num -= (digit*10**(power))
            print(num, power, digit)
            if digit == 4:
                ret += dict[str(power)][0]
            elif digit == 9:
                ret += dict[str(power)][1]
            elif digit >= 5:
                while digit -5 > 0:
                    ret += dict[str(power)][2]
                    digit -= 1
                ret += dict[str(power)][3]
            else:
                while digit > 0:
                    ret += dict[str(power)][2]
                    digit -= 1
    
            power += 1
        return ret[::-1]
            
