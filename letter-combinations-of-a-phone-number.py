class Solution(object):
    
    _dict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'],'4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z'], '0':[''], '1':['']}
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ret = []
        if not digits:
            return []
        prev = self.letterCombinations(digits[:-1])
        for char in self._dict[digits[-1]]:
            if not prev:
                ret += [char]
            else:
                ret += [x + char for x in prev]
        return ret
