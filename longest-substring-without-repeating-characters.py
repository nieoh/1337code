class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict = {}
        ret = 0
        i = 0
        sidx = 0
        while i < len(s):
            
            if s[i] in dict and dict[s[i]] >= sidx:
                ret = max(ret, i - sidx)
                sidx = dict[s[i]]+1
                dict[s[i]] = i
            else:
                dict[s[i]] = i
            i += 1
        
        ret = max(ret, i-sidx)
        return ret
        
